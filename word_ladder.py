#!/bin/python3

from collections import deque


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    dictionary_file = open('words5.dict', 'r')
    dictionary5 = dictionary_file.readlines()
    #replace variavle name in whiel loop w dicitornary5
    #make srue the readlinescommand works 
    stack = []
    stack.append(start_word)
    deque1 = deque([])
    deque1.append(stack)
    i=0
    while len(deque1) != 0:
        deque.popleft(stack)
        for i in range(len(dictionary_file)):
            if _adjacent(dictionary_file[i], stack[-1]) is True:
                    if dictionary_file[i] == end_word:
                        wordladder = deque1.popleft
                        wordladder.append(end_word)
                        return wordladder
                    stackcopy = stack.copy()
                    stackcopy.append(dictionary_file[i])
                    deque1.append(stackcopy)
                    #delete word from dictionary


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if len(ladder) == 1:
        return True
    if len(ladder) == 0:
        return False
    i = 0
    adjacentcounter = 0
    for i in (range(len(ladder)-1)):
        isadjacent = _adjacent(ladder[i], ladder[i+1])
        if isadjacent == True:
            adjacentcounter = adjacentcounter
        else:
            adjacentcounter += 1
    if adjacentcounter != 0:
        return False
    else:
        return True

def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    i = 0
    numberdifferentletters = 0
    for i in range(5): 
        if word1[i] == word2[i]:
            numberdifferentletters = numberdifferentletters
        else: 
            numberdifferentletters += 1
    if numberdifferentletters != 1:
        return False
    else:
        return True

