from Censored_lst import Censored_lst
from User import User
from Post import Post

def PostFilter(Post: str) -> str:
    if not Post:
        return "No Post in the input"

    Element_lst = Post.split(" ")
    for i in range(len(Censored_lst)):
        for j in range(len(Element_lst)):
            if Element_lst[j] == Censored_lst[i]:
                Element_lst[j] = "*" * len(Element_lst[j])

    Filtrated_lst = " ".join(Element_lst)
    return Filtrated_lst

def IsFeeding(postUser: User, Studied_Post: Post) -> bool:
    if(Studied_Post.Likes > postUser.Folowers):
        return True

    return False