artists_and_songs = {"Beyonce": ["Halo", "Run the World", "Irreplaceable"],
 "Maroon 5": ["Sugar", "Payphone", "Memories"],
  "Harry Styles": ["Sign of the Times", "Adore You", "Falling"], 
  "AC/DC": ["TNT", "It's a long way to the top", "Thunderstruck"]}
friends_artists = ["Maroon 5", "AC/DC", "Tame Impala"]


def playlist(a_dict, a_list):
    song_list = []
    for each_band in a_list:
        try:
            song_list.extend(a_dict[each_band])
        except KeyError:
            pass
    if not song_list:
        return "I guess I don't mind ads on the radio that much"
    return (sorted(song_list))

print(playlist(artists_and_songs, friends_artists))
    
