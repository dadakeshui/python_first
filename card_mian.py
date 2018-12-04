import card_tools

while True:

    #  显示功能菜单
    card_tools.show_menu()
    action_str=input("请选择希望执行的操作：")
    print("您选择的操作是【%s】"%action_str)

    #1,2,3针对名片的操作
    if action_str in ["1","2","3"]:
        #新增名片
        if action_str == "1":
            card_tools.new_card()
        #显示全部
        elif action_str == "2":
            card_tools.show_all()
        #查询名片
        elif action_str == "3":
            card_tools.search_card()
        pass
    # 0 退出系统
    elif action_str == "0":
        #如果在开发程序时，不希望立刻编写分支代码，可以使用pass关键字，表示一个占位符
        #能保证代码结构的正确
        print("您已经退出系统，欢迎再次使用【名片管理系统】")
        break
    else:
        print("您输入的不正确，请重新选择")




