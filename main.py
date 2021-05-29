
def main():
  hw = 'Hello World !'
  print(hw)
  with open('hello.txt','w') as f:
    f.write(hw)
  
  
if __name__ == '__main__':
  main()
