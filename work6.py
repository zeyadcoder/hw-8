class StringReverser:     
    def __init__(self, original_string):         
        self.original_string = original_string      
        def reverse_words(self):         
            words = self.original_string.split()         
            reversed_words = words[-1]         
            return ' '.join(reversed_words) 
        if __name__ == "__main__":     
            input_string = "reverse words"     
            reverser = StringReverser(input_string)     
            reversed_string = reverser.reverse_words()    
            print(reversed_string) 