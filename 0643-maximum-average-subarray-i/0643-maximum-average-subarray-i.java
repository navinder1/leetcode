class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int w=0;
        for(int i=0;i<k;i++){
            w+=nums[i];
        }
        int maxsum=w;
        for(int i=k;i<nums.length;i++){
            w=w-nums[i-k]+nums[i];
            if(w>maxsum){
                maxsum=w;
            }
        }
        return (double)maxsum/k;
    }
}