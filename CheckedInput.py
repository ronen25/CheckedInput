'''
A module that contains functions that check the input they get.

I wrote this module because I needed to write command-line programs that
checked their input. For example, one program needed to input numbers in
a certain range.
Writing input loops every time was tedious, so I decided to write a module for that.
'''
class CheckedInput:
    def input_number(prompt, min_, max_):
        '''
        Input a number and check if it's in range.
        The input loop will continue as long 
        num = None
        
        while True:
            # Input
            num = input(prompt)

            # Check if numeric
            try:
                num = int(num)
            except:
                print('error: input is not numeric')
                continue

            # Check bounds
            if min_ <= num <= max_:
                break
            else:
                print('error: number should be between {} and {}.'.format(min_, max_))

        return num

    def input_choice(prompt, choices):
        c = None

        while True:
            c = input(prompt)

            if c not in choices:
                print('error: options are: {}'.format(choices))
            else: break

        return c
        
    def input_numeric_list(prompt, choices):
        pass

    def input_yes_no(prompt):
        return input_choice(prompt, ['y', 'n', 'Y', 'N'])
