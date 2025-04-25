# Real Datasets 
Real datasets with Binary attributes.
We use the largest connected component.
Remove the nodes without attribute.
Without self loop edges.

All dataset has 2 files: edges.txt and attributes.txt

***
1) **Politicals Blogs**       https://websites.umich.edu/~mejn/netdata/


    Number of nodes: 1222
    Number of edges: 16714

A directed network of hyperlinks between weblogs on US politics. 
Political blogosphere Feb. 2005
Data compiled by Lada Adamic and Natalie Glance
Node "value" attributes indicate political leaning according to:
  0 (left or liberal)
  1 (right or conservative)
Data on political leaning comes from blog directories as indicated.  Some
blogs were labeled manually, based on incoming and outgoing links and posts
around the time of the 2004 presidential election.  Directory-derived
labels are prone to error; manual labels even more so.
Links between blogs were automatically extracted from a crawl of the front
page of the blog.
These data should be cited as Lada A. Adamic and Natalie Glance, "The
political blogosphere and the 2004 US Election", in Proceedings of the
WWW-2005 Workshop on the Weblogging Ecosystem (2005).
The graph is DISCONNECTED
- Number of components: 268
- Largest component size: 1222 nodes
- Fraction in largest component: 82.01%
Number of edges in largest component: 16714
Gender distribution:
- Female (1): 732 nodes
- Male (0): 758 nodes


***
2)  **Facebook Net**        http://www.sociopatterns.org/datasets/high-school-contact-and-friendship-networks/


    Number of nodes: 155
    Number of edges: 1412


This data set correspond to the contacts and friendship relations between students in a high school in Marseilles, France, in December 2013, as measured through several techniques.data set corresponds to the list of pairs of students for which the presence or absence of a Facebook friendship is known. Each line has the form “i j w”, where w=1 means that students i and j are linked on Facebook, while w=0 means that they are not. FACEBOOKNET consists of 155 vertices
and an edge between two students indicates friendship on
Facebook.  The fourth data set 

Initial graph:
- Nodes: 156
- Edges: 1437

After gender attribute processing:
- Removed 1 nodes without gender data
- Remaining nodes: 155
- Remaining edges: 1412

The graph is CONNECTED

Graph with gender attributes saved to 'fb_net_with_gender.gml'

Gender distribution:
- Female (1): 70 nodes
- Male (0): 85 nodes


***
3) **Books**         https://websites.umich.edu/~mejn/netdata/


    Number of nodes: 92
    Number of edges: 374


A network of books about US politics where edges 1 between books represented co-purchasing. 13 neutral. 49 conservative. 43 liberal. We use the dataset without neutral nodes. 


***
4) **Twitter**          https://networkrepository.com/

    Number of nodes: 18470
    Number of edges: 48053


A political retweet graph from "Ryan A. Rossi and Nesreen K. Ahmed. 2015.


***
5) **Drug net**        https://sites.google.com/site/ucinetsoftware/datasets/covert-networks/drugnet

   Number of nodes: 212
    Number of edges: 284

Number of nodes in the largest connected component: 190
Number of edges in the largest connected component: 270

This is a dichotomous adjacency matrix of drug users in Hartford.  Ties are directed and represent acquaintanceship. The network is a result of two years of ethnographic observations of people's drug habits.



***
6)  **Fiendship Net**        http://www.sociopatterns.org/datasets/high-school-contact-and-friendship-networks/   third one!!

Initial graph:
- Nodes: 134
- Edges: 406

After gender attribute processing:
- Removed 1 nodes without gender data
- Remaining nodes: 133
- Remaining edges: 401

The graph is DISCONNECTED
- Number of components: 3
- Largest component size: 127 nodes
- Fraction in largest component: 95.49%
- Number of nodes in the largest connected component: 127
Number of edges in the largest connected component: 396

Graph with gender attributes saved to 'fb_net_with_gender.gml'

Gender distribution:
- Female (1): 79 nodes
- Male (0): 54 nodes

The third data set corresponds to the directed network of reported friendships. Each line has the form “i j”, meaning that student i reported a friendship with student j.

***
7) **Facebook ego**     https://snap.stanford.edu/data/ego-Facebook.html
   
    Number of nodes: 4039
    Number of edges: 88234
   same characteristics as the largerst connected component. 
This dataset consists of 'circles' (or 'friends lists') from Facebook. Facebook data was collected from survey participants using this Facebook app. The dataset includes node features (profiles), circles, and ego networks. Protected attribute = gender.

***

8) **Deezer Europe **
   https://snap.stanford.edu/data/feather-deezer-social.html
Number of nodes: 28281
Number of edges: 92752
Number of nodes after removing nodes without attributes: 28281
Number of nodes in the largest connected component: 28281
Number of edges in the largest connected component: 92752
   
