# a_dict = {'burger king':[4,5,3,4,3], 'moes':[4,5,5,5,5], 'taco bell':[1,2,3,4,5]}
# value = 4.5
# min_rating = value

def restaurant_rating(a_dict, min_rating):
    """
    Returns all eligible restaurants above min_rating standard presend in a_dict
    """
    avg_rating_dict = {k:sum(v)/len(v) for k,v in a_dict.items()}  
    eligible_restaurants = [k for k,v in avg_rating_dict.items() if v >= min_rating] # create all eligible restaurant list
    # print(eligible_restaurants)
    # print(avg_rating_dict)
    return sorted(eligible_restaurants)

# print(restaurant_rating(a_dict, min_rating))