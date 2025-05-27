
artist= ['Jay-Z', "Britney"]
i = 0
time = 0
def chorus(artist, i):
    artist = artist[i]
    print(f''' My tummy's turnin' and I'm feelin' kinda homesick
Too much pressure and I'm nervous
That's when the DJ dropped my favorite tune
And a {artist} song was on
And a {artist} song was on
And a {artist} song was on
So I put my hands up
They're playin' my song, the butterflies fly away
I'm noddin' my head like, yeah
Movin' my hips like, yeah
I got my hands up, they're playin' my song
They know I'm gonna be okay
Yeah, it's a party in the U.S.A.
Yeah, it's a party in the U.S.A.''')
def SingSong(time):
    if time == 1:
        print(f'''I hopped off the plane at LAX
With a dream and my cardigan
Welcome to the land of fame excess (whoa)
Am I gonna fit in?
Jumped in the cab, here I am for the first time
Look to my right, and I see the Hollywood sign
This is all so crazy
Everybody seems so famous''')
    else:
        print(f'''Get to the club in my taxi cab
Everybody's looking at me now
Like, "Who's that chick that's rockin' kicks?
She gotta be from out of town"
So hard with my girls not around me
It's definitely not a Nashville party
'Cause all I see are stilettos
I guess I never got the memo''')
          
SingSong(time=1)
chorus(artist, i=0)
SingSong(time=2)
chorus(artist, i=1)
