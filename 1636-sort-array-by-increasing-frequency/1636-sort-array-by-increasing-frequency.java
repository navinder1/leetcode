class Solution {
    public int[] frequencySort(int[] nums) {

    Map<Integer, Integer> freq = new HashMap<>();

    for (int num : nums) {
        freq.put(num, freq.getOrDefault(num, 0) + 1);
    }

    
    return Arrays.stream(nums)
            .boxed()
            .sorted((a, b) -> {
                int frequencyCompare =
                        freq.get(a).compareTo(freq.get(b));

                if (frequencyCompare != 0) {
                    return frequencyCompare;
                }

                return Integer.compare(b, a);
            })
            .mapToInt(Integer::intValue)
            .toArray();

    }
}