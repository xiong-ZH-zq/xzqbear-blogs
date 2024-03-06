from itertools import permutations

def if_sorted(t:list) -> bool:
    # 检验是否排列成功
    for i in range(len(t)):
        if i+1 != t[i]:
            return False
    return True


def stack_sorting(t:iter) -> None:
    result = [] 
    stack = []
    for item in t:
        while stack and item >= stack[-1]:
            result.append(stack.pop())
        stack.append(item)
    
    # 将剩下的元素全部弹出
    while stack:
        result.append(stack.pop())
    
    return result

if __name__ == '__main__':
    # 对 1~n-1 的数列进行排序
    n = 10
    
    # permutations 用于生成所有排列
    arrs = permutations(range(1,n))
    max_iters = 0
    for arr in arrs:
        a = stack_sorting(arr)
        iters = 1
        while not if_sorted(a):
            iters += 1
            a = stack_sorting(a)
        
        max_iters = iters if max_iters < iters else max_iters
        print(f"{arr} 需要的排列次数为 {iters}")
    
    print(f"最大迭代次数为{max_iters}")