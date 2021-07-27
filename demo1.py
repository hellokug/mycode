import time
movies = ["八佰","花木兰","釜山行2"]

while True:
    print("##################################")
    print("欢迎来到电影管理系统")
    print("查看电影请按 1")
    print("增加电影请按 2")
    print("删除电影请按 3")
    print("修改电影请按 4")
    print("退出系统请按 0")
    print("##################################")
    order = input("请输入你的指令:")
    if order =="1":
        print("请稍后...")
        time.sleep(1)
        print("######电影列表#######")
        for movie in movies:
            print(movie)
        print("######电影列表#######")
    
    elif order=="2":
        movie = input("你要增加的电影是：")
        movies.append(movie)
        print("增加成功")
    elif order=="3":
        movie = input("你要删除的电影是：")
        if movie in movies:
            movies.remove(movie)
            print("删除成功")
        else:
            print("电影不存在")
    elif order =="4":
        movie = input("你要修改的电影是：")
        
        while movie not in movies:
            movie = input("电影不存在，请重新输入")
        movie1=input("你要将其修改成：")
        movies[movies.index(movie)]=movie1
        print("修改成功")
            
    elif order =="0":
        print("欢迎下次光临")
        break
    else:
        order=input("未知指令，请重新输入：")
        
    
    