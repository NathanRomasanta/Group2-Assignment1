class LexicalAnalyzer:
    def __init__(self):
        self.tokens = []

    def tokenize(self, user_input):
       
        self.tokens = user_input.split()
        return self.tokens

    def validate_tokens(self):
        numbers = []

        for token in self.tokens:

            #checks if token is a number
            try:
                number = float(token)
                print(f"Token '{token}' is a NUMBER")
                numbers.append(number)

            except ValueError:
                #if token is not a number, check what kind of token it is

                if token.isalpha():
                    #token contains only letters
                    print(f"Token '{token}' is a character token, please enter only numbers")

                elif token.isalnum():
                    #token contains both letters and numbers
                    print(f"Token '{token}' is a mixed token, please use a space to separate numbers and letters")

                else:
                    #token contains symbols like @, #, $, etc.
                    print(f"Token '{token}' is a symbol")

                raise ValueError("Invalid input detected. Please enter only numbers.")

        return numbers



class AverageParser:
    def __init__(self):
        self.analyzer = LexicalAnalyzer()

    def get_user_input(self):
      
        user_input = input("Enter numbers separated by spaces: ")
        return user_input

    def calculate_average(self, numbers):
       
        if len(numbers) == 0:
            raise ValueError("No numbers were provided.")

        total = sum(numbers)
        average = total / len(numbers)
        return average

    def run(self):
       
        try:
            user_input = self.get_user_input()

            # Tokenize input
            tokens = self.analyzer.tokenize(user_input)

            # Validate tokens
            numbers = self.analyzer.validate_tokens()

            # Calculate average
            average = self.calculate_average(numbers)

            print("\nTokens:", tokens)
            print("Valid Numbers:", numbers)
            print("Average:", average)

        except ValueError as e:
            print("\nError:", e)
        except Exception as e:
            print("\nUnexpected error:", e)


# Run the program
if __name__ == "__main__":
    parser = AverageParser()
    parser.run()
