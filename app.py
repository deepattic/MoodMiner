def main() -> None:
    comment: str = get_user_input()
    # step1
    comment: str = basic_filter(comment)
    # step2
    comment: list[str] = tokenize(comment)
    # step3
    comment: list[str] = stop_word_filter(comment)
    comment: list[str] = negation_handle(comment)
    # step4
    comment: list[str] = stem(comment)
    # step5
    stem_class: bool = feature_extract(comment)
    # if stem_class == True:
    #     print("good comment")
    # else:
    #     print("Bad comment")
    # I just use match function basically the same thing
    match stem_class:
        case True:
            print("This is a good Comment!")
        case False:
            print("This is a bad Comment!")

# This function get userinput and return it
def get_user_input() -> str:
    print("=> DEBUG: Getting User Input")
    comment: str = input("Enter Your Comment: ")
    return comment

# Sentiment analazis logic 

# Basic filtering
def basic_filter(comment: str) -> str:
    print("=> DEBUG: Applying Basic Filtering")
    #TODO: Add the logic
    return 'bar'

# Tokenization
# get the filtered input and return list of strings(tokenize)
def tokenize(comment: str) -> list[str]:
    print("=> DEBUG: Tokenizationing The Input")
    #TODO: Add the logic
    return ['bar']

# Stop word filter and Negation handling
# Hard part?
def stop_word_filter(l: list[str]) -> list[str]:
    print("=> DEBUG: Stop-Word Filtering")
    #TODO: Add the logic
    return ['bar']
def negation_handle(l: list[str]) -> list[str]:
    print("=> DEBUG: Negation Handling")
    #TODO: Add the logic
    return ['bar']

# Stemming
def stem(l: list[str]) -> list[str]:
    print("=> DEBUG: Stemming")
    #TODO: Add the logic
    return ['bar']

# decide good or bad comment using give word list
def feature_extract(l: list[str]) -> bool:
    return True


# This part is for run main funtion first caus i love funtional programming
if __name__ == '__main__':
    main()
