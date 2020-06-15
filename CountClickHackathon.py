#Author: Bhumi Patel

#The given function will take in an educational website and count the number
#of clicks it takes for users to reach privacy policy and end-user license agreement

'''
-> With the current pandemic, lives all around the world has been disturbed and
changed completely. With change in lifestyle and social behaviour, learning has
also been affected. Overnight schools were shutdown, universities need to close
their doors and educators, students, and parents needed to figure out ways to
keep learning continue, that adaptes to the "new normal." Online learning became
popular; however, security and privacy raised a huge concern as kids and learners
from all ages started learning online.

-> To address this huge we are trying to suggest a potential solution that involves
closly examing the educational sites and the amount of data they collect from
student learners. All the information that these sites collects makes users
vulnerable and affect their online presence and mental health.

-> With our solution we want users to have safe experience online and learn more
about these educational sites.

'''

#analyzing number of clicks required to search for privacy 


class click:
#using a binary tree to store website and privacy links    
    def __init__(self, web_link):
        self.random_links = []
        self.data = web_link

    #searching for target hit "privacy"
    def search_target(random_links, w_link): 
        for i in rnadom_links:
            if i.find("/privacy") != -1:
                w_link = i
            return w_link     #returns the string with privacy

    def distance_helper(node, target_link, distance):
        
        if node.data == target_link:
            return distance
        else:
            for j in range(len(node.random_links)):
                distance = distance_helper(node.random_links[i], target_link, distance+1)

                if distance == -1:
                    return -1
    

    def find_distance(root):
        return distance_helper(root, target_link, 0)
    

if __name__ == '__main__':


    #Step:1 load all the web_links in a N-ary tree
    #Step:2 find the link that contains privacy/policy
    #Step:3 pass that node in our distance function, to find how many clicks it takes to find privacy policy

    

#populating the list with privacy policies, terms of use agreements links, and other random links

#root objects for a N-ary tree known as Educational Websites
    root_n = click("https://www.khanacademy.org/")
    root_n.random_links.append(click("https://www.khanacademy.org/about/privacy-policy"))
    root_n.random_links.append(click("https://www.khanacademy.org/about/tos"))
    root_n.random_links[0].random_links.append(click("https://www.khanacademy.org/about/%7B%7B%22/about/api-tos%22%7Cpropagate_embedded%7D%7D"))
    root_n.random_links.append(click("https://www.khanacademy.org/science"))


    root_n1 = click("https://kahoot.com/")
    root_n1.random_links.append(click("https://kahoot.com/privacy-policy/"))
    root_n1.random_links.append(click("https://kahoot.com/study/"))
    root_n1.random_links[0].random_links.append(click("https://kahoot.com/schools/ways-to-play/"))
    root_n1.random_links[1].random_links.append(click("https://kahoot.com/home/learning-apps/dragonbox/"))
    

    root_n2 = click("https://code.org/")
    root_n2.random_links.append(click("https://studio.code.org/projects/public"))
    root_n2.random_links.append(click("https://code.org/about"))
    root_n2.random_links.append(click("https://code.org/promote"))
    root_n2.random_links.append(click("https://code.org/tos"))
    

    root_n3 = click("https://www.udemy.com/")
    root_n3.random_links.append(click("https://about.udemy.com/careers/?locale=en-us"))
    root_n3.random_links[0].random_links.append(click("https://about.udemy.com/tag/stories/"))
    root_n3.random_links[0].random_links[0].random_links.append(click("https://www.udemy.com/terms/copyright/"))
    root_n3.random_links.append(click("https://www.udemy.com/terms/privacy/"))
    
    
    
    #displays the number of clicks
    print("The number of click is" , find_distance(root_n))







    
