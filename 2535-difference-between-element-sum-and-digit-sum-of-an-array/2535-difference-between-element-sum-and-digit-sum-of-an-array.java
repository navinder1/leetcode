class Solution {
    public int differenceOfSum(int[] nums) {
        int ele=0;
        for(int val:nums){
            ele+=val;
        }
        int sum=0;
        for(int val:nums){
            int s=0;
            while(val>0){
                int temp=val%10;
                s+=temp;
                val/=10;
            }
            sum+=s;
        }
        return Math.abs(ele-sum);
    }
}