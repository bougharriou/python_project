from random 
def mnp2():
#n is the username
#d is dictionary with playlists’ names as keys
    d={}
        happy_songs = [
        "Here Comes the Sun - The Beatles",
        "Walking on Sunshine - Katrina & The Waves",
        "Don't Stop Me Now - Queen"
    ]
    sad_songs = [
        "Tears in Heaven - Eric Clapton",
        "Someone Like You - Adele",
        "The Sound of Silence - Simon & Garfunkel"
    ]
    energetic_songs = [
        "Eye of the Tiger - Survivor",
        "Uptown Funk - Mark Ronson ft. Bruno Mars",
        "Can't Stop - Red Hot Chili Peppers"
    ]
    rock_songs = [
        "Bohemian Rhapsody - Queen",
        "Hotel California - Eagles",
        "Stairway to Heaven - Led Zeppelin"
    ]
    pop_songs = [
        "Billie Jean - Michael Jackson",
        "Like a Prayer - Madonna",
        "Rolling in the Deep - Adele"
    ]
    jazz_songs = [
        "Take Five - Dave Brubeck",
        "What a Wonderful World - Louis Armstrong",
        "Feeling Good - Nina Simone"
    ]
    popular_songs = [
        "Imagine - John Lennon",
        "Let It Be - The Beatles",
        "Hallelujah - Leonard Cohen"
    ]


    print(f'Welcome to Music Playlist Manager!')
#  n:name
    n= input("Please enter your name: ")
    print(f'Please enter your name: {n}')
    print(f"Hello, {n} ! Let's start managing your Music Playlist !")

# # main menu
#  INFINITE LOOP.
    while True:
#  menu allowing the user to choose one from the listed items
        operation="choose an operation:"
        print(operation)
        print('1. Create/Edit a playlist')
        print('2. View playlists and number of songs contained')
        print('3. Shuffle and play')
        print('4. Get song recommendations')
        print('5. Exit')
        choice=input('Enter your choice (1-5):')
#  to handle any unexpected input; out of the range from 1 to 5
        if choice not in ['1','2','3','4','5']:
            print("Invalid choice. Try again.")
            continue
# The user selects operation 1
        if choice==1:
            while True:
                        print('1. Name a new playlist')
                        print('2. Add a song to a playlist')
                        print('3. Remove a song from a playlist')
                        print('4. Return to the main menu')
    
                        subchoice=input('Enter your choice (1-4):')
                        print(subchoice)
                        if subchoice not in ['1','2','3','4']:
                            print('try again')
                            continue
                        else:
# When option 1 is selected from the submenu
                            if subchoice=='1':
                                name_playlist=input("Name a new playlist:")
                                if name_playlist in d:
                                    print("This playlist already exists. Try another name.")
                                else:
                                    d[name_playlist] = {}  # new empty playlist
                                    print(f"Playlist '{name_playlist}' created.")
# the user selects operation 2 from the submenu 
                            elif subchoice=='2':
                                add_playlist=input('Which playlist you want to add a song to ?')
                                if  add_playlist in d:
                                    song_title=print('Enter song title:')
                                    artist=input('Enter artist')
# # #  the song title is the key and the artist name is the value   
                                    d[song_title] = artist
                                    print(f"'{song_title}' by {artist} added to '{add_playlist}'.")
                                else:
                                    print("Playlist not found. Try again.")
# # #   option 3 from the submenu     
                            elif subchoice=='3':
                                remove_song=input('Which playlist you want to remove a song from ?')
                                if remove_song in d:
                                    song_toremove=input('Enter song title to remove')
                                    if song_toremove in d[remove_song]:
                                        del d[remove_song][song_toremove]
                                        print(f"  '{song_toremove}' remove from '{remove_song}'.")
                                    else:
                                        print('song not in the playlist')
                                else:
                                    print("try again , we didn't found playlist")
# #  The user selects option 4 from the submenu
                            elif subchoice=='4':
# #     coming back to the main menu
                                break
# #    Back to the main menu, the user selects option 2 
                        elif choice=="2":
                            print("Your Playlists:")
                            if not d:
                                    print("No playlists available.")
                            else:
                                    i=1
                                    for playlist in d:
                                        print(str(i)+"."+playlist+"(d[playlist]))"+"songs")
                                        i=i+1
#  the user selects option 3
                        elif choice=="3":
                             playlist_name = input("Which playlist you want to shuffle a song from? ")
                             if playlist_name in d:
#the program shuffles and plays songs randomly from a playlist.

                                 song=random.choice(d[playlist_name])
                                 print(f'Now playing:{song}')
                            else:
                                print("try again")
# The user select option 4
                        elif choice == '4':
                            while True:
                                print('1. Mood-based Recommendation ')
                                print('2. Genre-based Recommendation')
                                print('3. Random Popular Song')
                                print('4. Return to the main menu')
                                inter_choice = input("Enter your choice (1-4): "):
# choosing option 1 from, a secondary submenu
                                if inter_choice=='1':
                                    while True:
                                        print('1. Happy')
                                        print('2. Sad')
                                        print('3. Energetic')
                                        print('4. Return to the primary submenu')
                                        x=input("enter your choice(1-4)")
# the three defined songs will be selected randomly
                                        if x not in ['1','2','3','4']:
                                            print("try again")
                                        elif x=='1':
                                             print("Now playing: ", random.choice(happy_songs))
                                        elif x=='2':
                                            print("Now playing: ", random.choice(sad_songs))
                                        elif x=='3':
                                            print("Now playing: :", random.choice(energetic_songs))
                                        elif x=='4':
                                            break
                                        else:
                                            print("Invalid choice.")
# #   choosing option 2 from the recommendation primary submenu          
                              elif inter_choice == '2':
                                  while True:
                                      print("1. Rock")
                                      print("2. Pop")
                                      print("3. Jazz")
                                      print("4. Return to the submenu")
                                      y=input("Enter your choice (1-4):")
                                      if y not in  ['1','2','3','4']:
                                          print("Invalid choice.")
#    one ofthe three defined songs will be selected randomly a
                                      elif y=='1':
                                          print("Now playing: ", random.choice(rock_songs))
                                      elif y=='2':
                                          print("Now playing: ", random.choice(pop_songs))
                                      elif y=='3':
                                          print("Now playing: ", random.choice(jazz_songs))
                                      else:
                                          break
#       the user chooses operation 3 in the primary submenu t
                              elif rec_choice == '3':
                                  print("Now playing: ", random.choice(popular_songs))
#     Option 4 in the secondary submenus is for coming back to the primary submenu
                             elif rec_choice == '4':
                                  break
# Option 4 in the primary submenu is for coming back to the main menu.
                              else:
                                  print("invalid try again")
                      else:
                              print("Hoping You Had Fun Creating Your Music Playlist Manager {n}")
                              break
                                
mnp2()
