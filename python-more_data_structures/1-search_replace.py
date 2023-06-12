#!/usr/bin/python3
def search_replace(my_list, search, replace):

#elem = element in my_list
    if (my_list):
        new_list = [replace if elem == search else elem for elem in my_list]
        return new_list
