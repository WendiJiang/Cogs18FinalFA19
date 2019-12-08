from chatbot import Chat,reflections,multiFunctionCall
import wikipedia
import string, webbrowser

movies = ['Following (1998)', 'Memento (2000)', 'Insomnia (2002)', 'Batman Begins (2005)',
         'The Prestige (2006)', 'The Dark Knight (2008)','Inception (2010)', 'The Dark Knight Rises (2012)',
         'Interstellar (2014)', 'Dunkirk (2017)', 'Tenet (2020)']

movie_set = ['Following', 'Memento', 'Insomnia', 'Batman Begins', 'The Prestige', 'The Dark Knight', 'Inception',
        'The Dark Knight Rises', 'Interstellar','Dunkirk', 'Tenet']

website_set = ['https://en.wikipedia.org/wiki/Following', 'https://en.wikipedia.org/wiki/Memento_(film)',
               'https://en.wikipedia.org/wiki/Insomnia_(2002_film)', 'https://en.wikipedia.org/wiki/Batman_Begins',
               'https://en.wikipedia.org/wiki/The_Prestige_(film)', 'https://en.wikipedia.org/wiki/The_Dark_Knight_(film)',
               'https://en.wikipedia.org/wiki/Inception', 'https://en.wikipedia.org/wiki/The_Dark_Knight_Rises',
               'https://en.wikipedia.org/wiki/Interstellar_(film)', 'https://en.wikipedia.org/wiki/Dunkirk_(2017_film)',
               'https://en.wikipedia.org/wiki/Tenet_(film)']

trailer_set = ['https://www.youtube.com/watch?v=udr4uX8uioo', 'https://www.youtube.com/watch?v=HDWylEQSwFo',
              'https://www.youtube.com/watch?v=brHA3CF4_Mw', 'https://www.youtube.com/watch?v=ceGXspGc2_4',
              'https://www.youtube.com/watch?v=o4gHCmTQDVI', 'https://www.youtube.com/watch?v=_PZpmTj1Q8Q'
              'https://www.youtube.com/watch?v=66TuSJo4dZM', 'https://www.youtube.com/watch?v=g8evyE9TuYk',
              'https://www.youtube.com/watch?v=0vxOhd4qlnA', 'https://www.youtube.com/watch?v=F-eMt3SrfFU',
              'Not available yet.']

def remove_punctuation(input_string):
    """
    this functions removes the punctuation inside the list for better output
    """
    out_string = ''
    for character in input_string:
        if character not in string.punctuation:
            out_string = out_string + character
    return out_string

def string_concatenator(string1, string2, seperator):
    output = string1 + seperator + string2
    return output

def list_to_string(input_list, seperator):
    """
    convert the input list into string variable, and split it with seperator
    """
    output = input_list[0]
    for item in input_list[1:]:
        output = string_concatenator(output, item, seperator)
    return output

def prepare_text(input_string):
    """
    this function prepares the input by removing puntuation, lowercase letter, and split the string
    """
    out_list = []
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    return out_list

def start_chat():
    """
    give a start for the chatbot
    """
    print('Hi, how are you?\n I can tell you more about Chritopher Nolan.\n Maybe you should start by type in his name. ;)\n')
    
def end_chat(input_list):
    """
    ends chatbot if quit is inside the input
    """
    if 'quit' in input_list:
        output = True
    else:
        output = False
    return output

def whoIs(query, sessionID = "general"):
    
    """
    this function is created to integrate the wikipedia API to the chatbot program
    """

    try:
        return wikipedia.summary(query)
    except:
        for newquery in wikipedia.search(query):
            try:
                return wikipedia.summary(newquery)
            except:
                pass
    return "I don't know about " + query
## this function is from the website I linked in the very beginning

def is_Movie(input_list):
    """
    Checks if the input asked for movies directed by Christopher Nolan
    """
    check = ''
    check = list_to_string(input_list, ' ')
    if 'movie' in check.lower() or 'movies' in check.lower():
        return True
    return False

def is_Wiki(input_list):
    """
    Checks if the input can be used for whoIs function
    """
    check = ''
    check = list_to_string(input_list, ' ')
    if whoIs(check.lower()) is not None:
        return True
    return False

def is_nolanLink(input_list):
    """ 
    Checks if the input asked for link of Nolan
    """
    check = ''
    check = list_to_string(input_list, ' ')
    if 'link' in check.lower() and 'nolan' in check.lower():
        return True
    return False

def is_movieLink(input_list):
    """
    Checks if the input asked for the link for the movie
    """
    check = ''
    check = list_to_string(input_list, ' ')
    for item in movie_set:
        if 'link' in check.lower() and list_to_string(item, '').lower() in check.lower():
            return True
    return False

def NolanBot():
    """
    main function to run the chatbot
    """
    chat = True
    start_chat()

    while chat:

        # Get a message from the user
        msg = input()
        out_msg = None
        other_msg = ''
        movie_index = 0
        
        # Prepare the input message
        msg = prepare_text(msg)
        nolan_link = is_nolanLink(msg)
        movie_link = is_movieLink(msg)
        

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'Bye!'
            chat = False
            
        
        # Check the type of variables
        elif is_Movie(msg):
            print("Here's the movies Christopher Nolan have directed:\n")
            out_msg = list_to_string(movies, ' ')
            other_msg = "If you want to know more about his film, pls type in the name, and will lead to the movie's wikipedia page, and give you a link for the film's trailer.\n"
            
        elif nolan_link:
            webbrowser.open('https://en.wikipedia.org/wiki/Christopher_Nolan')
            out_msg = 'View his wikipedia page for more information.'
            
        elif movie_link:
            for item in movie_set:
                if item.lower() in msg and 'link' in msg:
                    movie_index = movie_set.index(item)
            out_msg = "Here's the wikipedia page for " + movie_set[movie_index] + '\n' + website_set[movie_index]
            other_msg = 'Trailer link for ' + movie_set[movie_index] + ':\n' + trailer_set[movie_index]
            
        elif is_Wiki(msg):
            print("Here's the wikipedia description for " + list_to_string(msg, ' ') + ":\n")
            out_msg = whoIs(msg)
        
            
            
        print(out_msg, '\n\n', other_msg, '\n')
    