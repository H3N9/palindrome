
def maxArea(height):
    heightest = 0
    for i in range(len(height)):
        firstBar = int(height[i])
        for j in range(i + 1, len(height)):
            secondBar = int(height[j])
            diffBar = j - i
            diffHeight = max(firstBar, secondBar)-abs(firstBar-secondBar)
            container = diffBar * diffHeight
            if container > heightest:
                heightest = container
    return heightest


maxArea(input().split(" "))