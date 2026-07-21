class Song:
    def __init__(self,name):
        self.name=name
        self.next=None
class playlist:
    def __init__(self):
        self.head=None
    def add_song(self,song_name):
        new_song=Song(song_name)
        if self.head is None:
            self.head=new_song
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
                temp.next=new_song
            print(song_name,"added to playlist")
    def insert_song(self,position,song_name):
        new_song=Song(song_name)
        if position == 1:
            new_song.next=self.head
            self.head=new_song
            print(song_name,"inserted at position",position)
            return
        temp=self.head
        count=1
        while temp and count<position-1:
            temp=temp.next
            count+=1
            if temp is None:
                print("invalid Position")
            else:
                new_song.next=temp.next
                temp.next=new_song
                print(song_name,"inserted at position",position)
    def delete_song(self,song_name):
        temp=self.head
        if temp and temp.name==song_name:
            self.head=temp.next
            print(song_name,"deleted from playlist")
            return
        prev=None
        while temp and temp.name!=song_name:
            prey=temp
            temp=temp.next
        if temp is None:
            print("Song not found")
        else:
            prev.next=temp.next
            print(song_name,"deleted from playlist")
    def display(self):
        if self.head is None:
            temp=self.head
            print("\nplaylist is empty")
        else:
            temp=self.head
            print("\nMusic playlist:")
            while temp:
                print(temp.name,end="->")
                temp=temp.next
            print("None")
playlist=playlist()
while True:
    print("\n---Music Playlist Menu----")
    print("1.Create/Add Song")
    print("2.Insert Song")
    print("3.Delete Song")
    print("4.Display Playlist")
    print("5.exit")
    choice=int(input("Enter your choice:"))
    if choice == 1:
        song=input("enter song name")
        playlist.add_song(song)
    elif choice == 2:
        pos=int(input("enter position:"))
        song=input("enter song neme")
        playlist.insert_song(pos,song)
    elif choice == 3:
        song=input("enter song name to delete:")
        playlist.delete_song(song)
    elif choice == 4:
        playlist.display()
    elif choice == 5:
        print("Exiting Program")
        break
    else:
        print("invalid choice")
            
            
        
    
