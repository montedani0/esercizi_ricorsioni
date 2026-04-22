from time import sleep

#METODO ITERATIVO
def countdown(n):
    while n >= 0:
        print(n)
        sleep(1)
        n-=1

#METODO RICORSIVO
def countdown_recursive(n):
    if n==0:
        print("STOP")
    else:
        print(n)
        sleep(1)
        countdown_recursive(n-1)

if __name__ == '__main__':
    N = 4
    countdown_recursive(N)