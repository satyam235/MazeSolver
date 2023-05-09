import subprocess


if __name__ == '__main__':
    # create a menu for the user to select which demo to 
    while True:
        print('Select a demo to run:')
        print('1. A*')
        print('2. BFS')
        print('3. DFS')
        print('4. Quit')
        print('Enter a number: ')

        choice = input()
        if choice == '1':
            a_star = subprocess.Popen(['python', 'Demos/A-Star/aStarDemo.py'])
            try:
                a_star.wait()
            except KeyboardInterrupt:
            # If CTRL-C is pressed, terminate the subprocess
                a_star.terminate()
        if choice == '2':
            bfs = subprocess.Popen(['python', 'Demos/BFS/BFSDemo.py'])
            try:
                bfs.wait()
            except KeyboardInterrupt:

            # If CTRL-C is pressed, terminate the subprocess
                bfs.terminate()
        if choice == '3':
            dfs = subprocess.Popen(['python', 'Demos/DFS/DFSDemo.py'])
            try:
                dfs.wait()
            except KeyboardInterrupt:
            # If CTRL-C is pressed, terminate the subprocess
                dfs.terminate()
    
        if choice == '4':
            break
