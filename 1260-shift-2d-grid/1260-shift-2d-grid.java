class Solution {
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {

        int m = grid.length;
        int n = grid[0].length;

        k = k % (m * n);

        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            result.add(new ArrayList<>());

            for (int j = 0; j < n; j++) {

                int index = i * n + j;

                int oldIndex = (index - k + m * n) % (m * n);

                int oldRow = oldIndex / n;
                int oldCol = oldIndex % n;

                result.get(i).add(grid[oldRow][oldCol]);
            }
        }

        return result;
    }
}