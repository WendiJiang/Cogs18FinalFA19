from Cogs18Final_functions import *

test_list = ['start', 'bot']
test_string = 'start!bot'

def test_remove_punctuation():
    """
    test funtion for remove puntuation function
    """
    assert callable(remove_punctuation)
    assert isinstance(remove_punctuation(['hello,world']), str)
    assert remove_punctuation(prepare_text(test_string)) == 'startbot'
    
def test_string_concatenator():
    """
    test function for string concatenator funtion
    """
    assert callable(string_concatenator)
    assert isinstance(string_concatenator('start', 'bot', '!'), str)
    assert string_concatenator('start', 'bot', '!') == test_string

def test_list_to_string():
    """
    test function for list to string function
    """
    assert callable(list_to_string)
    assert isinstance(list_to_string(['hello world'],' '), str)
    assert list_to_string(['hello world'], ' ') == 'hello world'
    
def test_prepare_text():
    """
    test function for prepare text function
    """
    assert callable(prepare_text)
    assert isinstance(prepare_text(test_string), list)
    assert prepare_text(test_string) == ['startbot']
    
def test_end_chat():
    """
    test funtion for end chat funtion
    """
    assert callable(end_chat)
    assert isinstance(end_chat(test_list), bool)
    assert end_chat(test_list) == False
    
def test_whoIs():
    """
    test funtion for whoIs funtion
    """
    assert callable(whoIs)
    
def test_is_Movie():
    """
    test funtion for is_Movie funtion
    """
    assert callable(is_Movie)
    assert isinstance(is_Movie(['I want movie']), bool)
    assert is_Movie(['I want movie']) == True
    assert is_Movie(['I want']) == False
    
def test_is_Wiki():
    """
    test funtion for is_Wiki funtion
    """
    assert callable(is_Wiki)
    assert isinstance(is_Wiki(['christopher nolan']), bool)
    assert is_Wiki(['christopher nolan']) == True
    
def test_is_nolanLink():
    """
    test funtion for is_nolanLink funtion
    """
    assert callable(is_nolanLink)
    assert isinstance(is_nolanLink(['I want link for christopher nolan']), bool)
    assert is_nolanLink(['I want link for christopher nolan']) == True
    assert is_nolanLink(['I want link for christopher']) == False
    
def test_is_movieLink():
    assert callable(is_movieLink)
    assert isinstance(is_movieLink(['I want link for Following']), bool)
    assert is_movieLink(['I want link for Following']) == True
    assert is_movieLink(['I want link for christopher nolan']) == False

def test_all():
    """
    merge all test funtions together
    """
    test_remove_punctuation()
    test_string_concatenator()
    test_list_to_string()
    test_prepare_text()
    test_end_chat()
    test_whoIs()
    test_is_Movie()
    test_is_Wiki()
    test_is_nolanLink()
    test_is_movieLink()