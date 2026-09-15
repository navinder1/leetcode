class Solution {
    public String[] findRelativeRanks(int[] score) {

        PriorityQueue<Integer> pq =
            new PriorityQueue<>((a, b) -> score[b] - score[a]);

        String[] arr = new String[score.length];

        for (int i = 0; i < score.length; i++) {
            pq.add(i);
        }

        int rank = 1;

        while (!pq.isEmpty()) {

            int index = pq.poll();

            if (rank == 1) {
                arr[index] = "Gold Medal";
            } 
            else if (rank == 2) {
                arr[index] = "Silver Medal";
            } 
            else if (rank == 3) {
                arr[index] = "Bronze Medal";
            } 
            else {
                arr[index] = String.valueOf(rank);
            }

            rank++;
        }

        return arr;
    }
}