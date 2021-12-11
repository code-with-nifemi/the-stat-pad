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
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar

# Functions for finding occurrences of a pattern defined
# via a regular expression.
from re import *

# A function for displaying a web document in the host
# operating system's default web browser (renamed to
# distinguish it from the built-in "open" function for
# opening local files).
from webbrowser import open as urldisplay

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

# Setup the window and add a title:
GUI = Tk()
GUI.title('The Stat Pad - Stats in Seconds')
GUI.resizable(width = False, height = False)


# Assign HEX values to required colours:
colour_blue = '#032F4F'
colour_grey = '#333333'
colour_silver = '#f9f9f9'

GUI['bg'] = colour_silver

# Define Variables:
first_player_selection = StringVar()
second_player_selection = StringVar()
compare_player = BooleanVar()
compare_player_average = BooleanVar()



# Define function to compare Player 1 data to Player 2 data:
def compare_player_data():
    if (compare_player_average.get() == True) or ((compare_player_average.get() == False) and (second_player_selection.get("1.0", "end-1c") != '' and not second_player_selection.get("1.0", "end-1c").isspace())):    
        # Check if Player 1's PPG > Player 2's PPG, and highlight data accordingly:
        if float(PPG1_details['text']) > float(PPG2_details['text']):
            surplus = str(round(float(PPG1_details['text']) - float(PPG2_details['text']), 1))
            PPG1_details['fg'] = 'green'
            PPG2_details['fg'] = 'red'
            PPG1_details['text'] += ' (+' + surplus + ')'
        # Check if Player 1's PPG < Player 2's PPG, and highlight data accordingly:
        elif float(PPG1_details['text']) < float(PPG2_details['text']):
            surplus = str(round(float(PPG2_details['text']) - float(PPG1_details['text']), 1))
            PPG1_details['fg'] = 'red'
            PPG2_details['fg'] = 'green'
            PPG2_details['text'] += ' (+' + surplus + ')'
        else:
            # Statistics are equal:
            None

        # Check if Player 1's RPG > Player 2's RPG, and highlight data accordingly:
        if float(RPG1_details['text']) > float(RPG2_details['text']):
            surplus = str(round(float(RPG1_details['text']) - float(RPG2_details['text']), 1))
            RPG1_details['fg'] = 'green'
            RPG2_details['fg'] = 'red'
            RPG1_details['text'] += ' (+' + surplus + ')'
        # Check if Player 1's RPG < Player 2's RPG, and highlight data accordingly:
        elif float(RPG1_details['text']) < float(RPG2_details['text']):
            surplus = str(round(float(RPG2_details['text']) - float(RPG1_details['text']), 1))
            RPG1_details['fg'] = 'red'
            RPG2_details['fg'] = 'green'
            RPG2_details['text'] += ' (+' + surplus + ')'
        else:
            # Statistics are equal:
            None
            
        # Check if Player 1's APG > Player 2's APG, and highlight data accordingly:
        if float(APG1_details['text']) > float(APG2_details['text']):
            surplus = str(round(float(APG1_details['text']) - float(APG2_details['text']), 1))
            APG1_details['fg'] = 'green'
            APG2_details['fg'] = 'red'
            APG1_details['text'] += ' (+' + surplus + ')'
        # Check if Player 1's APG < Player 2's APG, and highlight data accordingly:
        elif float(APG1_details['text']) < float(APG2_details['text']):
            surplus = str(round(float(APG2_details['text']) - float(APG1_details['text']), 1))
            APG1_details['fg'] = 'red'
            APG2_details['fg'] = 'green'
            APG2_details['text'] += ' (+' + surplus + ')'
        else:
            # Statistics are equal:
            None
    else:
        # Check if 'Compare (Player vs NBA Average)' checkbox is disabled,
        # and return error message if so, as 'Player 2' is required:
        if compare_player_average.get() == False:
            Error_message['text'] = "*Please enter the name of a\n player into 'Player 2.'"

            PPG1_details['fg'] = 'black'
            RPG1_details['fg'] = 'black'
            APG1_details['fg'] = 'black'

            PPG2_details['fg'] = 'black'
            RPG2_details['fg'] = 'black'
            APG2_details['fg'] = 'black'

# Define function to compare Player 1 data to NBA average:
def compare_player_av():
    # Check if 'Player 2' is left blank, and return error message if not:
    if second_player_selection.get("1.0", "end-1c") != '' and not second_player_selection.get("1.0", "end-1c").isspace():
        Error_message['text'] = "*Please leave 'Player 2' blank."
        
        PPG1_details['fg'] = 'black'
        RPG1_details['fg'] = 'black'
        APG1_details['fg'] = 'black'

        PPG2_details['fg'] = 'black'
        RPG2_details['fg'] = 'black'
        APG2_details['fg'] = 'black'
    else:
        # Scrape calculate, and display NBA Average data:
        web_page_contents_average = download(url = 'https://www.basketball-reference.com/leagues/NBA_stats_per_game.html')
        PPG_av_re = '2021-22.+"pts_per_g" >([0-9.]+)</td>'
        PPG_av_scraped = findall(PPG_av_re, web_page_contents_average)
        PPG_av = str(round((float(PPG_av_scraped[0]) / 10), 1))
        PPG2_details['text'] = PPG_av

        RPG_av_re = '2021-22.+"trb_per_g" >([0-9.]+)</td>'
        RPG_av_scraped = findall(RPG_av_re, web_page_contents_average)
        RPG_av = str(round((float(RPG_av_scraped[0]) / 10), 1))
        RPG2_details['text'] = RPG_av

        APG_av_re = '2021-22.+"ast_per_g" >([0-9.]+)</td>'
        APG_av_scraped = findall(APG_av_re, web_page_contents_average)
        APG_av = str(round((float(APG_av_scraped[0]) / 10), 1))
        APG2_details['text'] = APG_av

        # Compare Player 1 data to NBA average data and highlight accordingly:
        compare_player_data()

        P2_Label['text'] = 'NBA Average'

# Define function to display player data:
def analyse_player_s():
    # Try to do the following:
    try:
        # Download page source as a string:
        web_page_contents = download(url = 'https://www.basketball-reference.com/leagues/NBA_2022_per_game.html')
        
        # Check if 'Player 1' is empty or only contains whitespace and return error message if so:
        if first_player_selection.get("1.0", "end-1c") == '' or first_player_selection.get("1.0", "end-1c").isspace(): 
            Error_message['text'] = "*Please enter the name of a\nplayer into 'Player 1'."
            return
        else:
            # Check if player's full name is entered and return error message if not:
            if len(first_player_selection.get("1.0", "end-1c").split(" ")) < 2 or first_player_selection.get("1.0", "end-1c").split(" ")[1] == '':
                Error_message['text'] = "*Please enter Player 1's full name."
                return
            else:
                # Assign first name, surname, and suffix to variables:
                Player1_firstname = first_player_selection.get("1.0", "end-1c").split(" ")[0]
                Player1_surname = first_player_selection.get("1.0", "end-1c").split(" ")[1]
                if len(first_player_selection.get("1.0", "end-1c").split(" ")) == 3:
                    Player1_suffix = first_player_selection.get("1.0", "end-1c").split(" ")[2]
                else:
                    Player1_suffix = ''
                
            # If name entered exists in data, scrape and display corresponding data:
            if first_player_selection.get("1.0", "end-1c") in web_page_contents:
                PPG1_re = 'csk="' + Player1_surname + ',' + Player1_firstname + '".+data-stat="pts_per_g" >(.+)</td'
                PPG1_scraped = findall(PPG1_re, web_page_contents)
                try:
                    PPG1_details['text'] = PPG1_scraped[0]

                    RPG1_re = 'csk="' + Player1_surname + ',' + Player1_firstname + '".+data-stat="trb_per_g" >([0-9.]+)</td'
                    RPG1_scraped = findall(RPG1_re, web_page_contents)
                    RPG1_details['text'] = RPG1_scraped[0]

                    APG1_re = 'csk="' + Player1_surname + ',' + Player1_firstname + '".+data-stat="ast_per_g" >([0-9.]+)</td'
                    APG1_scraped = findall(APG1_re, web_page_contents)
                    APG1_details['text'] = APG1_scraped[0]
                    
                    P1_Label['text'] = Player1_firstname, Player1_surname
                    if Player1_suffix != '':
                        P1_Label['text'] += '', Player1_suffix
                    else:
                        None

                    # Clear error message as analysis is successful:
                    Error_message['text'] = ''

                    PPG1_details['fg'] = 'black'
                    RPG1_details['fg'] = 'black'
                    APG1_details['fg'] = 'black'

                    PPG2_details['fg'] = 'black'
                    RPG2_details['fg'] = 'black'
                    APG2_details['fg'] = 'black'

                    PPG2_details['text'] = '--.-'
                    RPG2_details['text'] = '--.-'
                    APG2_details['text'] = '--.-'

                    P2_Label['text'] = 'Player 2'
        
                except:
                    Error_message['text'] = '*Data could not be sourced for Player 1.\nPlease correctly enter the name of an active\nplayer, with no leading or trailing spaces.'
                    return
            else:
                # Return error message as name entered does not exist in data:
                Error_message['text'] = '*Data could not be sourced for Player 1.\nPlease correctly enter the name of an active\nplayer, with no leading or trailing spaces.'
                return


            # Check if 'Player 2' contains non-whitespace characters and proceed with analysis if so:    
            if second_player_selection.get("1.0", "end-1c") != '' and not second_player_selection.get("1.0", "end-1c").isspace():
                # Check if player's full name is entered and return error message if not:
                if len(second_player_selection.get("1.0", "end-1c").split(" ")) < 2 or second_player_selection.get("1.0", "end-1c").split(" ")[1] == '':
                    Error_message['text'] = "*Please enter Player 2's full name."
                    return
                else:
                    # Assign first name, surname, and suffix to variables:
                    Player2_firstname = second_player_selection.get("1.0", "end-1c").split(" ")[0]
                    Player2_surname = second_player_selection.get("1.0", "end-1c").split(" ")[1]
                    if len(second_player_selection.get("1.0", "end-1c").split(" ")) == 3:
                        Player2_suffix = second_player_selection.get("1.0", "end-1c").split(" ")[2]
                    else:
                        Player2_suffix = ''
                # If name entered exists in data, scrape and display corresponding data:
                if second_player_selection.get("1.0", "end-1c") in web_page_contents:
                    PPG2_re = 'csk="' + Player2_surname + ',' + Player2_firstname + '".+data-stat="pts_per_g" >(.+)</td'
                    PPG2_scraped = findall(PPG2_re, web_page_contents)
                    try:
                        PPG2_details['text'] = PPG2_scraped[0]

                        RPG2_re = 'csk="' + Player2_surname + ',' + Player2_firstname + '".+data-stat="trb_per_g" >([0-9.]+)</td'
                        RPG2_scraped = findall(RPG2_re, web_page_contents)
                        RPG2_details['text'] = RPG2_scraped[0]

                        APG2_re = 'csk="' + Player2_surname + ',' + Player2_firstname + '".+data-stat="ast_per_g" >([0-9.]+)</td'
                        APG2_scraped = findall(APG2_re, web_page_contents)
                        APG2_details['text'] = APG2_scraped[0]

                        P2_Label['text'] = Player2_firstname, Player2_surname
                        if Player2_suffix != '':
                            P2_Label['text'] += '', Player2_suffix
                        else:
                            None

                        # Clear error message as analysis is successful:
                        Error_message['text'] = ''
                    except:
                        Error_message['text'] = '*Data could not be sourced for Player 2.\nPlease correctly enter the name of an active\nplayer, with no leading or trailing spaces.'
                        return
                else:
                    # Return error message as name entered does not exist in data:
                    Error_message['text'] = '*Data could not be sourced for Player 2.\nPlease correctly enter the name of an active\nplayer, with no leading or trailing spaces.'
                    return
            # No non-whitespace characters are entered into 'Player 2' - no need for analysis:
            else:
                None

            # Check if both 'Compare (Player vs Player)' and 'Compare (Player vs NBA Average)'
            # checkboxes are enabled and return error message if so:
            if compare_player.get() == True and compare_player_average.get() == True:
                Error_message['text'] = '*Please select only one checkbox.'

                PPG1_details['fg'] = 'black'
                RPG1_details['fg'] = 'black'
                APG1_details['fg'] = 'black'

                PPG2_details['fg'] = 'black'
                RPG2_details['fg'] = 'black'
                APG2_details['fg'] = 'black'
                return
            else:
                # If 'Compare (Player vs Player)' checkbox is enabled,
                # call function to compare Player 1 data to Player 2 data: 
                if compare_player.get() == True:
                    compare_player_data()
                    
                # If 'Compare (Player vs NBA Average)' checkbox is enabled,
                # call function to compare player data to NBA average:    
                if compare_player_average.get() == True:
                    compare_player_av()
        
    # Do the following in the case of an exception
    # where none of the errors above are the case:
    except:
        PPG1_details['text'] = '--.-'
        PPG1_details['font'] = ('Signika', 13, 'bold')
        RPG1_details['text'] = '--.-'
        RPG1_details['font'] = ('Signika', 13, 'bold')
        APG1_details['text'] = '--.-'
        APG1_details['font'] = ('Signika', 13, 'bold')

        PPG2_details['text'] = '--.-'
        PPG2_details['font'] = ('Signika', 13, 'bold')
        RPG2_details['text'] = '--.-'
        RPG2_details['font'] = ('Signika', 13, 'bold')
        APG2_details['text'] = '--.-'
        APG2_details['font'] = ('Signika', 13, 'bold')

        Error_message['text'] = '*Player analysis currently unavailable.'
        return
            

            
# Define function that directs user to view more
# information about 'Player 1' in browser:                
def view_more_stats_player1():
    # Check if 'Player 1' is empty or only contains whitespace and return error message if so:
    if first_player_selection.get("1.0", "end-1c") == '' or first_player_selection.get("1.0", "end-1c").isspace():
        Error_message['text'] = "*Please enter the name of a\nplayer into 'Player 1'."
        return
    elif len(first_player_selection.get("1.0", "end-1c").split(" ")) < 2:
        Error_message['text'] = "*Please enter Player 1's full name."
        return
    else:
        # Direct user to ESPN:
        url = 'https://www.espn.com/search/_/q/' + first_player_selection.get("1.0", "end-1c").split(" ")[0] + '%20' + first_player_selection.get("1.0", "end-1c").split(" ")[1]
        urldisplay(url)
        return
    
# Define function that directs user to view more
# information about 'Player 2' in browser: 
def view_more_stats_player2():
    # Check if 'Player 2' is empty or only contains whitespace and return error message if so:
    if second_player_selection.get("1.0", "end-1c") == '' or second_player_selection.get("1.0", "end-1c").isspace():
        Error_message['text'] = "*Please enter the name of a\nplayer into 'Player 2'."
        return
    elif len(second_player_selection.get("1.0", "end-1c").split(" ")) < 2:
        Error_message['text'] = "*Please enter Player 2's full name."
        return
    else:
        # Direct user to ESPN page, depending on
        # whether average data or player data is displayed:
        if compare_player_average.get() == True:
            url = 'https://www.espn.com.au/nba/stats'
        else:
            url = 'https://www.espn.com/search/_/q/' + second_player_selection.get("1.0", "end-1c").split(" ")[0] + '%20' + second_player_selection.get("1.0", "end-1c").split(" ")[1]
        urldisplay(url)
        return


#----------------------------------------------------------------#
    
# Create and display logo:
logo_image = PhotoImage(file='The_Stat_Pad_Logo.png')
logo = Label(GUI, image = logo_image, border = 0)
logo.grid(row = 1, column = 1, columnspan = 2)


# Create and display 'Player Selection' LabelFrame:
Selection = LabelFrame(GUI, text = 'Player Selection', labelanchor = 'n', fg = colour_blue, font = ('Signika', 15, 'bold'), bg = colour_silver)
Selection.grid(padx = 5, pady = 5, row = 2, column = 1, sticky = 'n')


# Create and display LabelFrames for each of two players to contain text entry fields:
First_player = LabelFrame(Selection, text = '*Player 1', labelanchor = 'n', fg = colour_grey, font = ('Signika', 13, 'bold'), bg = colour_silver)
First_player.grid(padx = 5, pady = 5, row = 1, column = 1)

second_player = LabelFrame(Selection, text = 'Player 2', labelanchor = 'n', fg = colour_grey, font = ('Signika', 13, 'bold'), bg = colour_silver)
second_player.grid(padx = 5, pady = 5, row = 2, column = 1)

# Create and display text entry fields for each of two players:
first_player_selection = Text(First_player, width = 25, height = 1, font = 11)
first_player_selection.grid(padx = 5, pady = 5, row = 1, column = 3, columnspan = 2)

second_player_selection = Text(second_player, width = 25, height = 1, font = 11)
second_player_selection.grid(padx = 5, pady = 5, row = 1, column = 3, columnspan = 2)


# Create and display 'Options' LabelFrame to contain user's options:
Options = LabelFrame(Selection, text = 'Options', labelanchor = 'n', fg = colour_grey, font = ('Signika', 13, 'bold'), bg = colour_silver)
Options.grid(padx = 5, pady = 5, row = 3, column = 1)

# Create and display 'Analyse' Button within 'Options' LabelFrame to analyse player data:
Analyse = Button(Options, text = 'Analyse', command = analyse_player_s, font = 11, activeforeground = 'white', activebackground = colour_blue)
Analyse.grid(padx = 5, pady = 5, row = 3, column = 1)

# Create and display 'Compare (Player vs Player)' Checkutton
# to provide option of comparing Player 1 to Player 2:
compare_button = Checkbutton(Options, text = 'Compare (Player vs Player)', variable = compare_player, onvalue = True, offvalue = False, font = 11, bg = colour_silver)
compare_button.grid(padx = 5, pady = 5, row = 1, column = 1, sticky = 'w')

# Create and display 'Compare (Player vs NBA Average)' Checkutton
# to provide option of comparing Player 1 to NBA Average:
compare_button = Checkbutton(Options, text = 'Compare (Player vs NBA Average)', variable = compare_player_average, onvalue = True, offvalue = False, font = 11, bg = colour_silver)
compare_button.grid(padx = 5, pady = 5, row = 2, column = 1, sticky = 'w')


# Create and display 'Player Selection' LabelFrame:
Selection_details = LabelFrame(GUI, text = 'Player Analysis', labelanchor = 'n', fg = colour_blue, font = ('Signika', 15, 'bold'), bg = colour_silver)
Selection_details.grid(padx = 5, pady = 5, row = 2, column = 2, sticky = 'n')

# Create and display 'Player Selection' LabelFrame to contain names of selected players:
Player_titles = LabelFrame(Selection_details, font = ('Signika', 15, 'bold'), bg = colour_blue)
Player_titles.grid(padx = 5, pady = 15, row = 1, column = 1, columnspan = 3, sticky = 'n')

# Create and display Labels to display names of selected players:
P1_Label = Label(Player_titles, text = '[Player 1]', justify = 'center', fg = 'white', font = ('Signika', 13, 'bold'), bg = colour_blue)
P1_Label.grid(pady = 5, row = 1, column = 1)

vs_Label = Label(Player_titles, text = 'vs', justify = 'center', width = 2, fg = 'white', font = ('Signika', 13, 'bold'), bg = colour_blue)
vs_Label.grid(pady = 5, row = 1, column = 2)

P2_Label = Label(Player_titles, text = '[Player 2]', justify = 'center', fg = 'white', font = ('Signika', 13, 'bold'), bg = colour_blue)
P2_Label.grid(pady = 5, row = 1, column = 3)


# Create and display Labels for each statistic:
PPG = Label(Selection_details, text = 'PPG', fg = colour_grey, font = ('Signika', 13, 'bold'), bg = colour_silver)
PPG.grid(padx = 5, pady = 5, row = 2, column = 2)

RPG = Label(Selection_details, text = 'RPG', fg = colour_grey, font = ('Signika', 13, 'bold'), bg = colour_silver)
RPG.grid(padx = 5, pady = 5, row = 3, column = 2)

APG = Label(Selection_details, text = 'APG', fg = colour_grey, font = ('Signika', 13, 'bold'), bg = colour_silver)
APG.grid(padx = 5, pady = 5, row = 4, column = 2)

# Create and display Labels to display Player 1's statistics:
PPG1_details = Label(Selection_details, text = '--.-', justify = 'center', font = 15, bg = colour_silver)
PPG1_details.grid(padx = 5, pady = 5, row = 2, column = 1)

RPG1_details = Label(Selection_details, text = '--.-', justify = 'center', font = 15,  bg = colour_silver)
RPG1_details.grid(padx = 5, pady = 5, row = 3, column = 1)

APG1_details = Label(Selection_details, text = '--.-', justify = 'center', font = 15,  bg = colour_silver)
APG1_details.grid(padx = 5, pady = 5, row = 4, column = 1)

# Create and display Labels to display Player 2's statistics:
PPG2_details = Label(Selection_details, text = '--.-', justify = 'center', font = 15, bg = colour_silver)
PPG2_details.grid(padx = 5, pady = 5, row = 2, column = 3)

RPG2_details = Label(Selection_details, text = '--.-', justify = 'center', font = 15,  bg = colour_silver)
RPG2_details.grid(padx = 5, pady = 5, row = 3, column = 3)

APG2_details = Label(Selection_details, text = '--.-', justify = 'center', font = 15,  bg = colour_silver, wraplength = 350)
APG2_details.grid(padx = 5, pady = 5, row = 4, column = 3)

# Create and display 'View More' buttons for each player for users to view more information:
View_more_p1 = Button(Selection_details, text = 'View More', command = view_more_stats_player1, font = 11, activeforeground = 'white', activebackground = colour_blue)
View_more_p1.grid(padx = 5, pady = 5, row = 5, column = 1)

View_more_p2 = Button(Selection_details, text = 'View More', command = view_more_stats_player2, font = 11, activeforeground = 'white', activebackground = colour_blue)
View_more_p2.grid(padx = 5, pady = 5, row = 5, column = 3)

# create and display 'Error Message' Label, where all error messages will be displayed:
Error_message = Label(Selection, text = '', justify = 'left', fg = 'red', font = ('Signika', 11), bg = colour_silver)
Error_message.grid(padx = 5, row = 4, column = 1, sticky = 'nw')

# Create and display 'Glossary' LabelFrame to contain glossary:
Glossary = LabelFrame(Selection_details, fg = colour_grey, font = ('Signika', 18, 'bold'), bg = colour_silver)
Glossary.grid(padx = 5, pady = 20, row = 6, column = 1, columnspan = 3, sticky = 's')

# Create and display 'Glossary Details' Label to provide explanation of statistics abbreviations:
Glossary_details = Label(Glossary, text = 'PPG: Points Per Game\nAPG: Assists Per Game\nRPG: Rebounds Per Game', font = 11, justify = "left", bg = colour_silver)
Glossary_details.grid(padx = 5, pady = 5, row = 1, column = 1, sticky = 'w')



# Start the event loop to react to user inputs:
GUI.mainloop()
