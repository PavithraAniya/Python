"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME =40
def bake_time_remaining(actual_mins):
    """Calculate remaining bake time based on expected bake time."""
    global EXPECTED_BAKE_TIME
    remaining_time = EXPECTED_BAKE_TIME - actual_mins
    return remaining_time

def preparation_time_in_minutes(no_of_layers):
    """Calculate preparation time based on the number of layers."""
    actual_mins= no_of_layers * 2
    return actual_mins

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Summary line.
    Calculate the elapsed cooking time.          
    This function takes two integers representing the number of lasagna             layers and the time already spent baking the lasagna. It calculates             the total elapsed minutes spent cooking (preparing + baking). 
    
    Parameters:         
        number_of_layers (int): The number of layers in the lasagna.                    elapsed_bake_time (int): Time the lasagna has been baking in the oven.          
    Returns:         
        int: The total time elapsed (in minutes) preparing and baking.     
        
      """
    total_time = preparation_time_in_minutes(number_of_layers)+ elapsed_bake_time
    return total_time

# print(elapsed_time_in_minutes(4,20))
