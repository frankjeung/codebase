




def to_usd(my_price):
    """
    This is a docstring. It tell us what this function is about. 
    What its reponsibilities are.
    What the params are about.
    What datatypes the params are.
    What this function will return.
    Example of invoking the function.

    This function formats the price of each item into USD.
    The function adds a dollar sign, and rounds decimals to nearest hundredth.
    The parameter is the unformatted price of each item.
    The parameter is a float datatype. 
    The function will return a formatted price with currency.

    Invoke like this: to_usd(9.9999)

    Example return value "$9.99"
    """
    return '${:,.2f}'.format(my_price)




## if this code is in the global scope
## ... of a file we're trying to import from
## ... it will throw errors when we try to run those other files
#price = input("Please choose a price like 4.9999")
#
#print(to_usd(float(price)))


if __name__ == "__main__":

    # nesting code in the main condition will
    # allow other scripts to cleanly import functions from this file
    # without running this code

    # this code still gets run when we invoke the script from the command line
    price = input("Please choose a price like 4.9999")

    print(to_usd(float(price)))
    