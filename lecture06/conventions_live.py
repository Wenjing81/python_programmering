def string_comparison_method(first_string:str, second_string:str):
    

    try:
        if first_string.lower()==second_string.lower():
            print("the strings are saying the same thing!")
        else:
            print("The strings are not saying the same thing:")
    except AttributeError:
        print("Hmm, one of your entries were not a sting at all")


def main():
    print("i'm in the main method")
    
    a=100
    b =1000
    print(a/b)

    string_to_print =string_comparison_method("hello world","Hello World")
    print(string_to_print)


    
