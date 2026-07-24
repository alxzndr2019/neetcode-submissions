class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();

        // Load the hashmap with default keys

        for (String str : strs) {
            char[] scharr = str.toCharArray();
            Arrays.sort(scharr);
            String s = new String(scharr);
            if (!map.containsKey(s)) {
                map.put(s, new ArrayList<>());
            } 
            map.get(s).add(str);
            
        }

        return new ArrayList<>(map.values());
    }
}
