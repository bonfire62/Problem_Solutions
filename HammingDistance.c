/*Explanation: The hamming distance between two numbers is the number of positions at which the bits are different:
e.g. for 4 and 2:
  4: 0100
  2: 0010
xor  0110
      ^^
Thus two of the bits are different. As shown above, the XOR operation is vital in this calculation. */

int hammingDistance(int x, int y){
int tmpInt=x^y;
int dis=0;

while(tmpInt)
{
    if(tmpInt & 1)
    {
        ++dis;
    }
    
    tmpInt>>=1;
}

return dis;
}
