class Solution {
    public boolean isAnagram(String s, String t) {
        //algorithim
        // compare lengths
        if(s.length() != t.length()){
            return false;
        }
        //Sort both s and t. amd compare
        char[] scharr = s.toCharArray();
        char[] tcharr = t.toCharArray();

        Arrays.sort(scharr);
        Arrays.sort(tcharr);

        String a = new String(scharr);
        String b = new String(tcharr);



        if(a.equals(b)){
            return true;
        }else{
            return false;
        }

    }
}
