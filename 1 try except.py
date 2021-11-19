while(True):
    print('Enter q to quit the game')
    q = input("Enter the no : ")\
    
    if q == 'q':
        break
    try :
        n = int(q)
        if n >6:
            print("No is greater than 6")

    except Exceptio as e:
        print(f"Error is : {e}")




























































