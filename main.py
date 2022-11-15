#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 20:57:19 2022

@author: farismismar
"""

import re

print('Instructions')
print('1) Using Google Chrome, login to your LinkedIn page and go to: https://www.linkedin.com/feed/followers/ to the bottom of the page')
print('2) Then using View | Developer | Developer Tools')
print('3) Find the line <html lang="en" class="theme theme...')
print('4) Right click and select Copy | Copy element')
print('5) Open a text editor and paste to the editor')
print('6) Save the file as followers_a.html')
print('7) Repeat instructions once more (on a different date) and call the resulting file followers_b.html')

filename_a = 'linkedinfollowers-20221105.html'
filename_b = 'linkedinfollowers-20221115.html'

def parse_followers(filename):
    f = open(filename, 'r')
    
    # read the whole file into memory
    file_buffer = f.read()
    f.close()
    
    pattern = '<h3 class="follows-recommendation-card__name t-14 t-black t-bold">\s+([^<]+$)'
    m = re.findall(pattern, file_buffer, re.MULTILINE)

    return m


followers_a = parse_followers(filename_a)
followers_b = parse_followers(filename_b)

difference = set(followers_a) - set(followers_b)
unfollowers = list(difference)

n = len(unfollowers)

print(f'Number of unfollowers: {n}')

if n > 0:    
    print('These unfollowers are: ', end='')
    for unfollower in unfollowers[:-1]:
        print(f'{unfollower}, ', end=',')
    print(unfollowers[-1])
