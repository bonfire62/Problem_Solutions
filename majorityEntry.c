/*This code assumes that there is a majority element, and that it constitutes n/2 of the given array.
It implements Moore's Voting Algorithm to increment or decrement a count based on the current array.
If the count drops below 0, it switches the majority index to the new element. Given that the array is
comprised of n/2 majority elements, it will always end with the majority element and the count >=1*/

int majorityElement(int* nums, int numsSize){

    int majIndex = 0, count = 1;
    int i;
    for(i = 1; i < numsSize; i++ ){
        if(nums[majIndex] == nums[i]){
            count++;
        }
        else{
            count--;
        }
        if(count == 0){
            majIndex = i;
            count = 1;
        }
    }
    return nums[majIndex];
}
