#-----Initialisation Steps-------------------------------------------#

# A function for exiting the program immediately (renamed
# because "exit" is already a standard Python function).
from sys import exit as abort

# A function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via the "download" function below.)
from urllib.request import urlopen

# Some standard Tkinter functions.
from tkinter import *

# Functions for finding occurrences of a pattern defined
# via a regular expression.
from re import *

# A function for displaying a web document in the host
# operating system's default web browser (renamed to
# distinguish it from the built-in "open" function for
# opening local files).
from webbrowser import open as urldisplay

import unicodedata

#---------------------------------------------#

def download(url = 'http://www.wikipedia.org/',
             target_filename = 'downloaded_document',
             filename_extension = 'html',
             save_file = True,
             char_set = 'UTF-8',
             incognito = False):

    # Import the function for opening online documents and
    # the class for creating requests
    from urllib.request import urlopen, Request

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        if incognito:
            # Pretend to be a web browser instead of
            # a Python script (NOT RELIABLE OR RECOMMENDED!)
            request = Request(url)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                               'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                               'Chrome/42.0.2311.135 Safari/537.36 Edge/12.246')
            print("Warning - Request does not reveal client's true identity.")
            print("          This is both unreliable and unethical!")
            print("          Proceed at your own risk!\n")
        else:
            # Behave ethically
            request = url
        web_page = urlopen(request)
    except ValueError:
        print("Download error - Cannot find document at URL '" + url + "'\n")
        return None
    except HTTPError:
        print("Download error - Access denied to document at URL '" + url + "'\n")
        return None
    except Exception as message:
        print("Download error - Something went wrong when trying to download " + \
              "the document at URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Read the contents as a character string
    try:
        web_page_contents = web_page.read().decode(char_set)
    except UnicodeDecodeError:
        print("Download error - Unable to decode document from URL '" + \
              url + "' as '" + char_set + "' characters\n")
        return None
    except Exception as message:
        print("Download error - Something went wrong when trying to decode " + \
              "the document from URL '" + url + "'")
        print("Error message was:", message, "\n")
        return None

    # Optionally write the contents to a local text file
    # (overwriting the file if it already exists!)
    if save_file:
        try:
            text_file = open(target_filename + '.' + filename_extension,
                             'w', encoding = char_set)
            text_file.write(web_page_contents)
            text_file.close()
        except Exception as message:
            print("Download error - Unable to write to file '" + \
                  target_filename + "'")
            print("Error message was:", message, "\n")

    # Return the downloaded document to the caller
    return web_page_contents

#----------------------------------------------------------------#

# Setup the GUI window and add a title
GUI = Tk()
GUI.resizable(width = False, height = False)
GUI.title('The Stat Pad - Stats in Seconds')

# Create colour variables (hexadecimal)
colour_blue = '#032F4F'
colour_grey = '#333333'
colour_silver = '#f9f9f9'

# Create font variables
labelframe_font = ('Signika', 15, 'bold')
stats_font = ('Signika', 15)
search_font_bold = ('Signika', 13, 'bold')
search_font = ('Signika', 13)
checkbutton_font = ('Signika', 12)
error_font = ('Signika', 11)
legend_font = ('Signika', 18, 'bold')

# Configure GUI background colour
GUI['bg'] = colour_silver

# Define checkbutton variables
compare_player2player = BooleanVar()
compare_player2average = BooleanVar()

# Define function to perform data analysis

def reset_data(player):

    if player == 1:

        P1_Label['text'] = '[Player 1]'

        PPG1_details['fg'] = 'black'
        RPG1_details['fg'] = 'black'
        APG1_details['fg'] = 'black'

        PPG1_details['text'] = '--.-'
        RPG1_details['text'] = '--.-'
        APG1_details['text'] = '--.-'

    elif player == 2:
        
        P2_Label['text'] = '[Player 2]'

        PPG2_details['fg'] = 'black'
        RPG2_details['fg'] = 'black'
        APG2_details['fg'] = 'black'

        PPG2_details['text'] = '--.-'
        RPG2_details['text'] = '--.-'
        APG2_details['text'] = '--.-'

        
# Define function that directs user to view more
# information about a given player in the user's browser               
def view_more(player):

    if player == 1:

        try:

            p1_name = P1_Label['text']
                
            # Check if 'Player 1' is empty or only contains whitespace and return error message if so:
            if (p1_name == '[Player 1]'):
                selection_error_message['text'] = "*Please analyse Player 1's statistics."

                return
            
            else:
                    
                p1_firstname = p1_name.split()[0]
                p1_surname = p1_name.split()[1]
                
                # Direct user to ESPN:
                url = f"https://www.espn.com/search/_/q/{p1_firstname}%20{p1_surname}"
                urldisplay(url)
                return
        except:
            selection_error_message['text'] = f"*Unable to provide more information on {p1_name}."
            
    elif player == 2:
        
        try:

            p2_name = P2_Label['text']

            # Check if 'Player 1' is empty or only contains whitespace and return error message if so:
            if (p2_name == '[Player 2]'):
                selection_error_message['text'] = "*Please analyse Player 2's statistics."

                return

            elif p2_name == 'NBA Average':
                    url = 'https://www.espn.com.au/nba/stats'
            else:
                
                p2_firstname = p2_name.split()[0]
                p2_surname = p2_name.split()[1]
            
                # Direct user to ESPN:
                url = f"https://www.espn.com/search/_/q/{p2_firstname}%20{p2_surname}"
                    
            urldisplay(url)
            return
        
        except:
            selection_error_message['text'] = f"*Unable to provide more information on {p2_name}."
    

def retrieve_data(first_name, surname, html_code):

    if first_name == 'NBA' and surname == 'Average':

        PPG_regex = f'''csk="[a-zA-Z,\.\-À-Ÿ ']+".+data-stat="pts_per_g" >([0-9.]+)</td'''
        PPG_stats = findall(PPG_regex, html_code)
        PPG = f'{round(sum(map(float, PPG_stats)) / len(PPG_stats), 1)}'

        RPG_regex = f'''csk="[a-zA-Z,\.\-À-Ÿ ']+".+data-stat="trb_per_g" >([0-9.]+)</td'''
        RPG_stats = findall(RPG_regex, html_code)
        RPG = f'{round(sum(map(float, RPG_stats)) / len(RPG_stats), 1)}'
        
        APG_regex = f'''csk="[a-zA-Z,\.\-À-Ÿ ']+".+data-stat="ast_per_g" >([0-9.]+)</td'''
        APG_stats = findall(APG_regex, html_code)
        APG = f'{round(sum(map(float, APG_stats)) / len(APG_stats), 1)}'
        
    else:
        
        PPG_regex = f'''csk="{surname},{first_name}".+data-stat="pts_per_g" >([0-9.]+)</td'''
        PPG_stats = findall(PPG_regex, html_code)
        PPG = PPG_stats[0]

        RPG_regex = f'''csk="{surname},{first_name}".+data-stat="trb_per_g" >([0-9.]+)</td'''
        RPG_stats = findall(RPG_regex, html_code)
        RPG = RPG_stats[0]

        APG_regex = f'''csk="{surname},{first_name}".+data-stat="ast_per_g" >([0-9.]+)</td'''
        APG_stats = findall(APG_regex, html_code)
        APG = APG_stats[0]

    return PPG, RPG, APG
    
def compare_stats():

        # Retrive statistics and compute relative difference for each respective category

        # Points Per Game
        PPG1 = float(PPG1_details['text'])
        PPG2 = float(PPG2_details['text'])
        PPG_difference = round(PPG1 - PPG2, 1)

        # Rebounds Per Game
        RPG1 = float(RPG1_details['text'])
        RPG2 = float(RPG2_details['text'])
        RPG_difference = round(RPG1 - RPG2, 1)

        # Assists Per Game
        APG1 = float(APG1_details['text'])
        APG2 = float(APG2_details['text'])
        APG_difference = round(APG1 - APG2, 1)

        
        # Check relative difference for each respective category and highlight data accordingly

        # Points Per Game
        if PPG_difference > 0:
            PPG1_details['fg'] = 'green'
            PPG2_details['fg'] = 'red'
            PPG1_details['text'] += f' (+{PPG_difference})'
        elif PPG_difference < 0:
            PPG1_details['fg'] = 'red'
            PPG2_details['fg'] = 'green'
            PPG2_details['text'] += f' (+{-PPG_difference})'

        # Rebounds Per Game
        if RPG_difference > 0:
            RPG1_details['fg'] = 'green'
            RPG2_details['fg'] = 'red'
            RPG1_details['text'] += f' (+{RPG_difference})'
        elif RPG_difference < 0:
            RPG1_details['fg'] = 'red'
            RPG2_details['fg'] = 'green'
            RPG2_details['text'] += f' (+{-RPG_difference})'

        # Assists Per Game
        if APG_difference > 0:
            APG1_details['fg'] = 'green'
            APG2_details['fg'] = 'red'
            APG1_details['text'] += f' (+{APG_difference})'
        elif APG_difference < 0:
            APG1_details['fg'] = 'red'
            APG2_details['fg'] = 'green'
            APG2_details['text'] += f' (+{-APG_difference})'
        

# Define function to retreive and process statistics
def analyse_stats():
    
    # Attempt the following:
    try:

        # Check if both checkbuttons are selected -- display error message if so
        if (compare_player2player.get() and compare_player2average.get()):

            option_error_message['text'] = '*Please select only one checkbox.'
            selection_error_message['text'] = ''
            return
        else:
            option_error_message['text'] = ''
        
        # Download webpage source code as a string
        web_page_contents = download(url = 'https://www.basketball-reference.com/leagues/NBA_2024_per_game.html')

        # Convert accented characters to their non-accented counterparts
        nfkd_form = unicodedata.normalize('NFKD', web_page_contents)

        web_page_contents = ''.join([c for c in nfkd_form if not unicodedata.combining(c)]).lower()

        # Retreive search entries from user input fields
        p1_name = p1_selection.get("1.0", "end-1c").strip().lower()
        p2_name = p2_selection.get("1.0", "end-1c").strip().lower()
        
        # Check if 'Player 1' input field is empty, only contains whitespace or
        # doesn't contain the player's full name -- display error message if so
        if p1_name == '' or p1_name.isspace() or len(p1_name.split()) < 2:
            
            # Display error message
            selection_error_message['text'] = "*Please enter Player 1's full name."

            # Restore default data for Player 1
            reset_data(player = 1)

            return          
            
        # At this point in the program, valid input for Player 1 has been confirmed
        else:
            
            # Assign Player 1's first name and surname to variables
            p1_firstname, p1_surname = p1_name.split()[:2]
                
            # Attempt to retrieve Player 1's statistics
            try:

                PPG1_details['text'], RPG1_details['text'], APG1_details['text'] = \
                                      retrieve_data(p1_firstname, p1_surname, web_page_contents)

                # Update Player 1 label text
                P1_Label['text'] = f'{" ".join(p1_name.split())}'.title()
                

                # Clear error message as data retrieval is successful
                selection_error_message['text'] = ''

                # Reset font colour (for statistics) to black (in case currently highlighted)
                PPG1_details['fg'] = 'black'
                RPG1_details['fg'] = 'black'
                APG1_details['fg'] = 'black'


            # Display error message and restore default data as statistics cannot be retrieved for user input
            except:

                # Display error message
                selection_error_message['text'] = f'*Data could not be sourced for "{p1_name.title()}".'

                # Restore default data for Player 1
                reset_data(player = 1)
                
                return

            # At this point in the program, data has been successfully retrieved for Player 1
            # The program will proceed to assess user input for Player 2

            # Do the following in the case that neither checkbutton is selected
            if not (compare_player2player.get() or compare_player2average.get()):

                # Check if 'Player 2' input field is empty or only contains whitespace -- restore
                # default data for Player 2 and exit function if so
                if (p2_name == '' or p2_name.isspace()):

                    # Restore default data for Player 2
                    reset_data(player = 2)
                    
                    return
                
                # Check if Player 2's full name is entered -- display error message if not
                elif len(p2_name.split()) < 2:

                    # Display error message
                    selection_error_message['text'] = "*Please enter Player 2's full name."

                    # Restore default data for Player 2
                    reset_data(player = 2)
                    
                    return
                
                # At this point in the program, valid input for Player 2 has been confirmed
                else:

                    # Assign Player 2's first name and surname to variables
                    p2_firstname, p2_surname = p2_name.split()[:2]
                        

                    # Attempt to retrieve Player 2's statistics
                    try:

                        # Retrieve and display Player 2's statistics
                        PPG2_details['text'], RPG2_details['text'], APG2_details['text'] = \
                                                  retrieve_data(p2_firstname, p2_surname, web_page_contents)

                        # Update Player 2 label text with name of player
                        P2_Label['text'] = f'{" ".join(p2_name.split())}'.title()
                        
                        # Clear error message as data retrieval is successful
                        selection_error_message['text'] = ''

                        # Reset font colour (for statistics) to black (in case currently highlighted)
                        PPG2_details['fg'] = 'black'
                        RPG2_details['fg'] = 'black'
                        APG2_details['fg'] = 'black'

                        return


                    # Display error message and restore default data as statistics cannot be retrieved for user input
                    except:

                        # Display error message
                        selection_error_message['text'] = f'*Data could not be sourced for "{p2_name.title()}".'

                        # Restore default data for Player 2
                        reset_data(player = 2)
                        
                        return                  

            else:

                # Do the following in the case that the first checkbutton is selected
                if compare_player2player.get():

                    # Check if 'Player 1' input field is empty, only contains whitespace or
                    # doesn't contain the player's full name -- display error message if so
                    if p2_name == '' or p2_name.isspace() or len(p2_name.split()) < 2:

                        # Display error message
                        selection_error_message['text'] = "*Please enter Player 2's name."

                        # Restore default data for Player 2
                        reset_data(player = 2)
                        
                        return
                    
                    else:
                        
                        # Assign first name, surname, and suffix to variables:
                        p2_firstname, p2_surname = p2_name.split()[:2]
                            
                        # Attempt to retrieve Player 2's statistics
                        try:

                            # Retrieve and display Player 2's statistics
                            PPG2_details['text'], RPG2_details['text'], APG2_details['text'] = \
                                                  retrieve_data(p2_firstname, p2_surname, web_page_contents)

                            # Update Player 2 label text with name of player
                            P2_Label['text'] = f'{" ".join(p2_name.split())}'.title()
                            
                            # Clear error message as data retrieval is successful
                            selection_error_message['text'] = ''

                            # Reset font colour (for statistics) to black (in case currently highlighted)
                            PPG2_details['fg'] = 'black'
                            RPG2_details['fg'] = 'black'
                            APG2_details['fg'] = 'black'


                        # Display error message and restore default data as statistics cannot be retrieved for user input
                        except:

                            # Display error message
                            selection_error_message['text'] =  f'*Data could not be sourced for "{p2_name.title()}".'

                            # Restore default data for Player 2
                            reset_data(player = 2)
                            
                            return  

                # Do the following in the case that the second checkbutton is selected
                elif compare_player2average.get():

                    # Clear user input for Player 2
                    if not (p2_name == '' or p2_name.isspace()):
                        p2_selection.delete(0.0, END)

                    # Attempt to retrieve NBA Average statistics
                    try:

                        # Retrieve and display Player 2's statistics
                        PPG2_details['text'], RPG2_details['text'], APG2_details['text'] = \
                                              retrieve_data('NBA', 'Average', web_page_contents)
                        
                        # Update Player 2 label text
                        P2_Label['text'] = 'NBA Average'
                        

                        # Clear error message as data retrieval is successful
                        selection_error_message['text'] = ''

                        # Display error message and restore default data as statistics cannot be retrieved for user input
                        PPG2_details['fg'] = 'black'
                        RPG2_details['fg'] = 'black'
                        APG2_details['fg'] = 'black'


                    # Display error message and restore default data as statistics cannot be retrieved for user input
                    except:

                        # Display error message
                        selection_error_message['text'] = '*Data could not be sourced for NBA Average statistics.'

                        # Restore default data for Player 2
                        reset_data(player = 2)
                        
                        return 

                # Perform statistical comparison        
                compare_stats()
                
                return   
        
    # Do the following in the case of an exception
    # where none of the errors above are the case:
    except:
        
        # Display error message
        selection_error_message['text'] = '*Player analysis currently unavailable.'

        # Restore default data for both players
        reset_data(player = 1)
        reset_data(player = 2)
        
        return


#----------------------------------------------------------------#
    
# Create and display logo
logo_image = PhotoImage(file='The_Stat_Pad_Logo_2.png')
logo = Label(GUI, image = logo_image, border = 0)
logo.grid(row = 1, column = 1, columnspan = 2)


# Create and display 'Player Selection' LabelFrame
Selection = LabelFrame(GUI, text = 'Player Selection', labelanchor = 'n', fg = colour_blue, font = labelframe_font, \
                       bg = colour_silver)
Selection.grid(padx = 5, pady = (5, 0), row = 2, column = 1, sticky = 'n')


# Create and display LabelFrames for entry fields for each player
p1 = LabelFrame(Selection, text = '*Player 1', labelanchor = 'n', fg = colour_grey, font = search_font_bold, \
                          bg = colour_silver)
p1.grid(padx = 20, pady = 5, row = 1, column = 1)

p2 = LabelFrame(Selection, text = 'Player 2', labelanchor = 'n', fg = colour_grey, font = search_font_bold, \
                           bg = colour_silver)
p2.grid(padx = 20, pady = 5, row = 2, column = 1)


# Create and display text entry fields for each player
p1_selection = Text(p1, width = 30, height = 1, font = search_font)
p1_selection.grid(padx = 5, pady = 5, row = 1, column = 3, columnspan = 2)

p2_selection = Text(p2, width = 30, height = 1, font = search_font)
p2_selection.grid(padx = 5, pady = 5, row = 1, column = 3, columnspan = 2)


# Create and display 'Options' LabelFrame to contain user's options
Options = LabelFrame(GUI, text = 'Options', labelanchor = 'n', fg = colour_blue, font = labelframe_font, bg = colour_silver)
Options.grid(padx = 5, pady = 5, row = 3, column = 1)


# Create and display 'Analyse' Button within 'Options' LabelFrame to analyse player data
Analyse = Button(Selection, text = 'Analyse', command = analyse_stats, font = search_font, activeforeground = 'white', \
                 activebackground = colour_blue)
Analyse.grid(padx = 5, pady = (5, 5), row = 3, column = 1)


# Create and display Checkbutton to provide option of comparing players
compare_button = Checkbutton(Options, text = 'Compare (Player 1 vs Player 2)', \
                             variable = compare_player2player, onvalue = True, offvalue = False, \
                             font = checkbutton_font, bg = colour_silver)
compare_button.grid(padx = 20, pady = (5, 0), row = 1, column = 1, sticky = 'w')


# Create and display Checkutton to provide option of comparing Player 1 to NBA Average
compare_button = Checkbutton(Options, text = 'Compare (Player 1 vs NBA Average)', \
                             variable = compare_player2average, onvalue = True, offvalue = False, \
                             font = checkbutton_font, bg = colour_silver)
compare_button.grid(padx = 20, pady = (0, 5), row = 2, column = 1, sticky = 'w')


# Create and display 'Player Selection' LabelFrame
Selection_details = LabelFrame(GUI, text = 'Player Analysis', labelanchor = 'n', fg = colour_blue, \
                               font = labelframe_font, bg = colour_silver)
Selection_details.grid(padx = 5, pady = 5, row = 2, column = 2, rowspan = 2, sticky = 'n')


# Create and display 'Player Selection' LabelFrame to contain names of selected players
Player_titles = LabelFrame(Selection_details, bg = colour_blue)
Player_titles.grid(padx = 5, pady = 15, row = 1, column = 1, columnspan = 3, sticky = 'n')


# Create and display Labels to display names of selected players
P1_Label = Label(Player_titles, width = 12, wraplength = 150, text = '[Player 1]', justify = 'center', fg = 'white', \
                 font = search_font_bold, bg = colour_blue)
P1_Label.grid(padx = (5, 0), pady = 5, row = 1, column = 1)

vs_Label = Label(Player_titles, text = 'vs', justify = 'center', width = 2, fg = 'white', font = search_font_bold, \
                 bg = colour_blue)
vs_Label.grid(padx = 10, pady = 5, row = 1, column = 2)

P2_Label = Label(Player_titles, width = 12, wraplength = 150, text = '[Player 2]', justify = 'center', fg = 'white', \
                 font = search_font_bold, bg = colour_blue)
P2_Label.grid(padx = (0, 5), pady = 5, row = 1, column = 3)


# Create and display Labels for each statistic:
PPG = Label(Selection_details, text = 'PPG', fg = colour_grey, font = search_font_bold, bg = colour_silver)
PPG.grid(padx = 0, pady = 5, row = 2, column = 2)

RPG = Label(Selection_details, text = 'RPG', fg = colour_grey, font = search_font_bold, bg = colour_silver)
RPG.grid(padx = 0, pady = 5, row = 3, column = 2)

APG = Label(Selection_details, text = 'APG', fg = colour_grey, font = search_font_bold, bg = colour_silver)
APG.grid(padx = 0, pady = 5, row = 4, column = 2)


# Create and display Labels to display Player 1's statistics
PPG1_details = Label(Selection_details, text = '--.-', justify = 'center', font = stats_font, bg = colour_silver)
PPG1_details.grid(padx = (5, 0), pady = 5, row = 2, column = 1)

RPG1_details = Label(Selection_details, text = '--.-', justify = 'center', font = stats_font,  bg = colour_silver)
RPG1_details.grid(padx = (5, 0), pady = 5, row = 3, column = 1)

APG1_details = Label(Selection_details, text = '--.-', justify = 'center', font = stats_font,  bg = colour_silver)
APG1_details.grid(padx = (5, 0), pady = 5, row = 4, column = 1)


# Create and display Labels to display Player 2's statistics
PPG2_details = Label(Selection_details, text = '--.-', justify = 'center', font = stats_font, bg = colour_silver)
PPG2_details.grid(padx = (0, 5), pady = 5, row = 2, column = 3)

RPG2_details = Label(Selection_details, text = '--.-', justify = 'center', font = stats_font,  bg = colour_silver)
RPG2_details.grid(padx = (0, 5), pady = 5, row = 3, column = 3)

APG2_details = Label(Selection_details, text = '--.-', justify = 'center', font = stats_font,  bg = colour_silver, \
                     wraplength = 350)
APG2_details.grid(padx = (0, 5), pady = 5, row = 4, column = 3)


# Create and display 'View More' buttons for users to view more information about each player
View_more_p1 = Button(Selection_details, text = ' View More ', command = lambda: view_more(player = 1), font = search_font, \
                      activeforeground = 'white', activebackground = colour_blue)
View_more_p1.grid(padx = (10, 0), pady = 5, row = 5, column = 1)

View_more_p2 = Button(Selection_details, text = ' View More ', command = lambda: view_more(player = 2), font = search_font, \
                      activeforeground = 'white', activebackground = colour_blue)
View_more_p2.grid(padx = (0, 10), pady = 5, row = 5, column = 3)


# Create and display 'Error Message' Labels, where all error messages will be displayed
selection_error_message = Label(Selection, text = '', justify = 'left', fg = 'red', font = error_font, bg = colour_silver)
selection_error_message.grid(padx = 5, row = 4, column = 1, sticky = 'nw')

option_error_message = Label(Options, text = '', justify = 'left', fg = 'red', font = error_font, bg = colour_silver)
option_error_message.grid(padx = 5, row = 3, column = 1, sticky = 'nw')


# Create and display 'Legend' LabelFrame to contain legend
Legend = LabelFrame(Selection_details, fg = colour_grey, font = legend_font, bg = colour_silver)
Legend.grid(padx = 5, pady = (18, 5), row = 6, column = 1, columnspan = 3, sticky = 'sw')


# Create and display 'Legend Details' Label to provide explanation of statistics abbreviations
Legend_details = Label(Legend, text = 'PPG: Points Per Game\nAPG: Assists Per Game\nRPG: Rebounds Per Game', \
                         font = search_font, justify = "left", bg = colour_silver)
Legend_details.grid(padx = (5, 100), pady = 5, row = 1, column = 1, sticky = 'w')


# Start the event loop to react to user inputs:
GUI.mainloop()
