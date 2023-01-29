#this program reads groups of numbers separated by blank lines from  
#an input file, totals those groups and finds the largest total

def main():
        #open and read the file
        infile=open('input-1-1.txt', 'r')
        file_contents = infile.read()

        #create a list where each group is an item in the list
        group = file_contents.split('\n\n')
        num_list=[]
        
        #loop through all items, creating sub-lists
        #loop through those sub-lists, converting each str to int and totaling
        #append totals back to num_list
        i = 0
        while i < len(group):
                subgroup = (group[i].splitlines())      
                totaled_numbers = []                    
 
                for item in subgroup:
                        num = int(item)                 
                        totaled_numbers.append(num)     
                
                num_list.append(sum(totaled_numbers))

                i += 1

        infile.close()

        #print the max number from num_list
        print(max(num_list))
        
#call the main function
if __name__=='__main__':
	main()