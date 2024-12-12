import tkinter as tk
from tkinter import ttk, messagebox


# Define a class to represent a Song
class Song:
    def __init__(self, title: str, artist: str, mood: str, genre: str):
        """
        Initialize a song with title, artist, mood, and genre.
        :param title: Title of the song.
        :param artist: Artist of the song.
        :param mood: Mood category for the song.
        :param genre: Genre of the song.
        """
        self.title = title
        self.artist = artist
        self.mood = mood
        self.genre = genre


# Function to create a list of predefined songs
def create_song_library():
    """
    Create a library of songs with different moods and genres.
    :return: List of Song objects.
    """
    return [
        Song("Happy", "Pharrell Williams", "happy", "pop"),
        Song("Someone Like You", "Adele", "sad", "pop"),
        Song("Lose Yourself", "Eminem", "motivated", "hip-hop"),
        Song("All of Me", "John Legend", "romantic", "R&B"),
        Song("Don't Stop Believin'", "Journey", "motivated", "rock"),
        Song("Fix You", "Coldplay", "sad", "rock"),
        Song("Perfect", "Ed Sheeran", "romantic", "pop"),
        Song("Happy Together", "The Turtles", "happy", "pop"),
        Song("Eye of the Tiger", "Survivor", "motivated", "rock"),
        Song("What a Wonderful World", "Louis Armstrong", "happy", "jazz"),
    ]


# Function to recommend songs based on the user's mood
def recommend_songs():
    mood = mood_var.get()
    if mood == "Select your mood":
        messagebox.showinfo("Rhythm", "Please select a valid mood.")
        return

    recommendations = [
        f"{song.title} by {song.artist}" for song in song_library if song.mood.lower() == mood.lower()
    ]

    if recommendations:
        messagebox.showinfo(
            "Recommended Songs",
            f"Songs for your mood '{mood}':\n" + "\n".join(recommendations),
        )
    else:
        messagebox.showinfo("Recommended Songs", f"No songs found for the mood '{mood}'.")


# Function to add a song to the favorites list
def add_to_favorites():
    song_title = favorites_entry.get()
    if song_title:
        favorite_songs.append(song_title)
        favorites_entry.delete(0, tk.END)
        update_favorites_list()
    else:
        messagebox.showinfo("Rhythm", "Please enter a song title to add to favorites.")


# Function to update the favorites list in the UI
def update_favorites_list():
    favorites_listbox.delete(0, tk.END)
    for song in favorite_songs:
        favorites_listbox.insert(tk.END, song)


# Function to search for songs based on title or artist
def search_song():
    search_term = search_entry.get().lower()
    if not search_term:
        messagebox.showinfo("Rhythm", "Please enter a search term.")
        return

    search_results = [
        f"{song.title} by {song.artist}" for song in song_library
        if search_term in song.title.lower() or search_term in song.artist.lower()
    ]

    if search_results:
        messagebox.showinfo("Search Results", "\n".join(search_results))
    else:
        messagebox.showinfo("Search Results", "No songs found.")


# Function to recommend songs based on genre
def recommend_by_genre():
    genre = genre_var.get()
    if genre == "Select genre":
        messagebox.showinfo("Rhythm", "Please select a valid genre.")
        return

    recommendations = [
        f"{song.title} by {song.artist}" for song in song_library if song.genre.lower() == genre.lower()
    ]

    if recommendations:
        messagebox.showinfo(
            "Recommended Songs by Genre",
            f"Songs for the genre '{genre}':\n" + "\n".join(recommendations),
        )
    else:
        messagebox.showinfo("Recommended Songs by Genre", f"No songs found for the genre '{genre}'.")


# Function to display a custom playlist
def create_playlist():
    playlist_name = playlist_entry.get()
    if playlist_name:
        custom_playlists.append(playlist_name)
        playlist_entry.delete(0, tk.END)
        update_playlist_list()
    else:
        messagebox.showinfo("Rhythm", "Please enter a playlist name.")


# Function to update the playlist list in the UI
def update_playlist_list():
    playlist_listbox.delete(0, tk.END)
    for playlist in custom_playlists:
        playlist_listbox.insert(tk.END, playlist)


# Create the song library and other data structures
song_library = create_song_library()
favorite_songs = []
custom_playlists = []

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Rhythm")  # App name as "Rhythm"
root.geometry("500x600")  # Set the window size
root.configure(bg="#f0f8ff")  # Light blue background color

# Create a Notebook (Tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Create individual tabs
mood_tab = ttk.Frame(notebook)
favorites_tab = ttk.Frame(notebook)
search_tab = ttk.Frame(notebook)
genre_tab = ttk.Frame(notebook)
playlist_tab = ttk.Frame(notebook)
artist_tab = ttk.Frame(notebook)

# Add tabs to the notebook
notebook.add(mood_tab, text="Mood Songs")
notebook.add(favorites_tab, text="Favorites")
notebook.add(search_tab, text="Search Songs")
notebook.add(genre_tab, text="Genres")
notebook.add(playlist_tab, text="Playlists")
notebook.add(artist_tab, text="Recommended Artists")

# --- Mood-based song recommendation tab ---
title_label = tk.Label(
    mood_tab,
    text="Rhythm",
    font=("Helvetica", 18, "bold"),
    bg="#f0f8ff",
    fg="#4682b4",  # Steel blue text color
)
title_label.pack(pady=20)

mood_label = tk.Label(
    mood_tab, text="Select your mood:", font=("Helvetica", 14), bg="#f0f8ff", fg="#333"
)
mood_label.pack(pady=5)

mood_var = tk.StringVar()
mood_var.set("Select your mood")
mood_menu = tk.OptionMenu(
    mood_tab, mood_var, "happy", "sad", "motivated", "romantic"
)
mood_menu.config(font=("Helvetica", 12), bg="#87ceeb", fg="#000", width=20)
mood_menu["menu"].config(font=("Helvetica", 12))
mood_menu.pack(pady=10)

recommend_button = tk.Button(
    mood_tab,
    text="Recommend Songs",
    command=recommend_songs,
    font=("Helvetica", 14, "bold"),
    bg="#32cd32",  # Lime green color
    fg="white",
    relief="raised",
    borderwidth=3,
)
recommend_button.pack(pady=15)

# --- Favorites tab ---
favorites_label = tk.Label(
    favorites_tab, text="Favorite Songs", font=("Helvetica", 14, "bold"), bg="#f0f8ff"
)
favorites_label.pack(pady=10)

favorites_entry = tk.Entry(favorites_tab, font=("Helvetica", 12))
favorites_entry.pack(pady=10)

add_button = tk.Button(
    favorites_tab,
    text="Add to Favorites",
    command=add_to_favorites,
    font=("Helvetica", 14),
    bg="#32cd32",  # Lime green color
    fg="white",
    relief="raised",
)
add_button.pack(pady=10)

favorites_listbox = tk.Listbox(favorites_tab, width=40, height=10, font=("Helvetica", 12))
favorites_listbox.pack(pady=10)

# --- Search tab ---
search_label = tk.Label(
    search_tab, text="Search Songs", font=("Helvetica", 14, "bold"), bg="#f0f8ff"
)
search_label.pack(pady=10)

search_entry = tk.Entry(search_tab, font=("Helvetica", 12))
search_entry.pack(pady=10)

search_button = tk.Button(
    search_tab,
    text="Search",
    command=search_song,
    font=("Helvetica", 14),
    bg="#4682b4",  # Steel blue color
    fg="white",
    relief="raised",
)
search_button.pack(pady=10)

# --- Genre tab ---
genre_label = tk.Label(
    genre_tab, text="Select a Genre", font=("Helvetica", 14, "bold"), bg="#f0f8ff"
)
genre_label.pack(pady=10)

genre_var = tk.StringVar()
genre_var.set("Select genre")
genre_menu = tk.OptionMenu(genre_tab, genre_var, "pop", "rock", "hip-hop", "R&B", "jazz")
genre_menu.config(font=("Helvetica", 12), bg="#87ceeb", fg="#000", width=20)
genre_menu["menu"].config(font=("Helvetica", 12))
genre_menu.pack(pady=10)

genre_recommend_button = tk.Button(
    genre_tab,
    text="Recommend by Genre",
    command=recommend_by_genre,
    font=("Helvetica", 14),
    bg="#32cd32",  # Lime green color
    fg="white",
    relief="raised",
)
genre_recommend_button.pack(pady=10)

# --- Playlist tab ---
playlist_label = tk.Label(
    playlist_tab, text="Create a Playlist", font=("Helvetica", 14, "bold"), bg="#f0f8ff"
)
playlist_label.pack(pady=10)

playlist_entry = tk.Entry(playlist_tab, font=("Helvetica", 12))
playlist_entry.pack(pady=10)

create_playlist_button = tk.Button(
    playlist_tab,
    text="Create Playlist",
    command=create_playlist,
    font=("Helvetica", 14),
    bg="#32cd32",  # Lime green color
    fg="white",
    relief="raised",
)
create_playlist_button.pack(pady=10)

playlist_listbox = tk.Listbox(playlist_tab, width=40, height=10, font=("Helvetica", 12))
playlist_listbox.pack(pady=10)

# --- Recommended Artists tab ---
artist_label = tk.Label(
    artist_tab, text="Recommended Artists", font=("Helvetica", 14, "bold"), bg="#f0f8ff"
)
artist_label.pack(pady=10)

messagebox.showinfo("Rhythm", "Artists will be displayed here in future versions.")

# Run the Tkinter event loop
root.mainloop()
