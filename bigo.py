"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Sujani Srinivasan and Meghna Prabhakaran, this 
programming assignment is my own work and I have not provided this code to 
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: sps2996
UT EID 2: mp52744
"""


# TODO: implement this function. You may delete this comment when you are done.
def length_of_longest_substring_n3(s):
   max_length = 0
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            # Check if the substring s[i:j+1] has all unique characters
            substring = s[i:j+1]
            if len(set(substring)) == len(substring):
                max_length = max(max_length, len(substring))
    return max_length

    


# TODO: implement this function. You may delete this comment when you are done.
def length_of_longest_substring_n2(s):
    max_length = 0
    n = len(s)
    for i in range(n):
        freq = [0] * 256
        for j in range(i, n):
            char_index = ord(s[j])
            freq[char_index] += 1
            if freq[char_index] > 1:
                break
            max_length = max(max_length, j - i + 1)
    return max_length
    


# TODO: implement this function. You may delete this comment when you are done.
def length_of_longest_substring_n(s):
    max_length = 0
    n = len(s)
    start = 0
    freq = [0] * 256
    for end in range(n):
        char_index = ord(s[end])
        freq[char_index] += 1
        while freq[char_index] > 1:
            freq[ord(s[start])] -= 1
            start += 1
        max_length = max(max_length, end - start + 1)
    return max_length