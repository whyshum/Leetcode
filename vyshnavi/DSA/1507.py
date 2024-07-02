class Solution:
    def reformatDate(self, date: str) -> str:
        
        month={'Jan': '01', 'Feb': '02', 
                'Mar': '03', 'Apr': '04', 
                'May': '05', 'Jun': '06', 
                'Jul': '07', 'Aug': '08', 
                'Sep': '09', 'Oct': '10', 
                'Nov': '11', 'Dec': '12'}
        words = date.split(' ')
        print(date[:2])
        if(int(words[0][:-2])>9):
            return words[-1]+"-"+ month[words[1]]+"-"+date[:2]
        else:
            return words[-1]+"-"+ month[words[1]]+"-"+'0'+date[:1]