# -*- coding: utf-8 -*-
"""垃圾分类小助手（规则版）

输入一种垃圾的名字，程序告诉你它属于哪一类，并给出一句投放提示。
这是一个轻量的规则版示例，后续可以用机器学习模型替换规则。
"""

# 关键词表：命中任意一个关键词，就归到对应的类别
RULES = {
    "可回收物": ["纸箱", "报纸", "书本", "塑料瓶", "易拉罐", "金属", "玻璃", "衣服", "饮料罐", "铁", "铝", "纸"],
    "有害垃圾": ["电池", "灯管", "灯泡", "药品", "药片", "温度计", "油漆", "杀虫剂", "荧光灯", "水银"],
    "厨余垃圾": ["剩饭", "菜叶", "果皮", "香蕉皮", "苹果核", "鱼骨", "鸡蛋壳", "茶叶", "骨头", "花瓣", "面包"],
    "其他垃圾": ["纸巾", "卫生纸", "尿布", "烟头", "陶瓷", "一次性餐具", "尘土", "贝壳", "创可贴"],
}

# 每一类的投放提示
TIPS = {
    "可回收物": "清空、洗净、沥干后投放。",
    "有害垃圾": "请单独投放，注意不要弄破包装。",
    "厨余垃圾": "沥干水分，去掉包装袋后投放。",
    "其他垃圾": "尽量沥干水分后投放。",
}


def classify(name):
    """返回垃圾所属的类别，识别不出时返回 None。"""
    name = (name or "").strip()
    if not name:
        return None
    for category, keywords in RULES.items():
        for kw in keywords:
            if kw in name:
                return category
    return None


def main():
    print("=" * 34)
    print(" 垃圾分类小助手（规则版）")
    print(" 输入垃圾名称，我来告诉你怎么分。")
    print(" 输入 q 退出。")
    print("=" * 34)
    while True:
        name = input("\n请输入垃圾名称：").strip()
        if name.lower() in ("q", "quit", "exit", "退出"):
            print("再见，记得好好分类哦 👋")
            break
        category = classify(name)
        if category:
            print(f"→ 「{name}」属于：{category}")
            print(f"   提示：{TIPS[category]}")
        else:
            print(f"→ 暂时没识别出「{name}」，建议按当地标准投放到「其他垃圾」，或问一下社区分类指引。")


if __name__ == "__main__":
    main()
