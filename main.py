from random import randint
start = 1
end = 1000

val = randint(start, end)

print('''\n Rules for the game :-
      
 1) You should guess number between {0} to {1} .
 
 2) You will be notified if Your number is higher or lower.
 
 3) If you guessed it right you will win the game.
 
 4) You have only 10 chanse to guesss it.
 
 :-) :-) :-) :-) :-) :-) :-) :-) :-) :-) :-) 
 
Best Of Luck\n'''.format(start, end))




for i in range(9,0,-1):
    
    ch = int(input('Your Guess ? '))
    
    if ch>0 and ch<1001:
        print('Remaining Guess :',i)
        if ch > val and abs(ch-val) > 2:
            print('Your Guess is higher than the number.')
        elif ch < val and abs(ch-val) > 2:
            print('Your Guess is lower than the number.')
        elif ch == val:
            print('You guessed it right. :-)')
            break
            exit
        else:
            print('You guess is very near to the Number !! ')
    else:
        print('Invalid Entry. :-( Please try again')

if i <= 1:
    print('you Failled the game..')
    print('Correct number was :',val)