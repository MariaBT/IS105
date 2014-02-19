# Variables with string-values
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who know %s." % (binary, do_not)

# Print strings from variables above
print x
print y

# Print strings in strings 
print "I said: %r." % x
print "I also said: '%s'." % y

#===================================================================
# Variables 
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Print strings from variables above
print joke_evaluation % hilarious

#===================================================================
# Variables
w = "This is the left side of..."
e = "a string with a right side."

# Print the results of variables 
print w + e
