
# and ((touching.left >= touched.left and touching.left <= touched.right) or(touching.right >= touched.left and touching.right <= touched.right)
# ((touching.left >= touched.left and touching.left <= touched.right) or (touching.right >= touched.left and touching.right <= touched.right))


def bottomCollision(touching, touched):
    # or (touching.right >= touched.left and touching.right <= touched.right)
    if touching.bottom <= touched.bottom and touching.bottom >= touched.top and ((touched.left >= touching.left and touched.left <= touching.right) or (touched.right >= touching.left and touched.right <= touching.right) or (touching.left >= touched.left and touching.left <= touched.right)):
        return 1
    else:
        return 0


def topCollision(touching, touched):
    if touching.top <= touched.bottom and touching.top >= touched.top and ((touched.left >= touching.left and touched.left <= touching.right) or (touched.right >= touching.left and touched.right <= touching.right) or (touching.left >= touched.left and touching.left <= touched.right) or (touching.right >= touched.left and touching.right <= touched.right)):
        return 1
    else:
        return 0


def leftCollision(touching, touched):
    # or (touching.right >= touched.left and touching.right <= touched.right)
    if touching.left <= touched.right and touching.left >= touched.left and ((touched.top >= touching.top and touched.top <= touching.bottom) or (touched.bottom >= touching.top and touched.bottom <= touching.bottom) or (touching.bottom >= touched.top and touching.bottom <= touched.bottom)):
        return 1
    else:
        return 0


def rightCollision(touching, touched):
    # or (touching.right >= touched.left and touching.right <= touched.right)
    if touching.right <= touched.right and touching.right >= touched.left and ((touched.top >= touching.top and touched.top <= touching.bottom) or (touched.bottom >= touching.top and touched.bottom <= touching.bottom) or (touching.bottom >= touched.top and touching.bottom <= touched.bottom)):
        return 1
    else:
        return 0


def sideCollision(touching, touched):
    top = False
    bottom = False
    left = False
    right = False

    # or (touching.right >= touched.left and touching.right <= touched.right)
    if touching.bottom <= touched.bottom and touching.bottom >= touched.top and ((touched.left >= touching.left and touched.left <= touching.right) or (touched.right >= touching.left and touched.right <= touching.right) or (touching.left >= touched.left and touching.left <= touched.right)):
        bottom = True
    elif touching.top <= touched.bottom and touching.top >= touched.top and ((touched.left >= touching.left and touched.left <= touching.right) or (touched.right >= touching.left and touched.right <= touching.right) or (touching.left >= touched.left and touching.left <= touched.right) or (touching.right >= touched.left and touching.right <= touched.right)):
        top = True
    # or (touching.right >= touched.left and touching.right <= touched.right)
    if touching.left <= touched.right and touching.left >= touched.left and ((touched.top >= touching.top and touched.top <= touching.bottom) or (touched.bottom >= touching.top and touched.bottom <= touching.bottom) or (touching.bottom >= touched.top and touching.bottom <= touched.bottom)):
        left = True
    # or (touching.right >= touched.left and touching.right <= touched.right)
    if touching.right <= touched.right and touching.right >= touched.left and ((touched.top >= touching.top and touched.top <= touching.bottom) or (touched.bottom >= touching.top and touched.bottom <= touching.bottom) or (touching.bottom >= touched.top and touching.bottom <= touched.bottom)):
        right = True

    if bottom:
        horizontalTouch = abs(touching.width - (abs(touching.left - touched.left)))
        verticalTouch = abs(touching.height - (abs(touching.top - touched.top))) / 1.5
        if left and right:
            return ('bottom')
        elif left:
            if horizontalTouch > verticalTouch:
                return ('bottom')
            else:
                return ('left')
        elif right:
            if horizontalTouch > verticalTouch:
                return ('bottom')
            else:
                return ('right')
        else:
            return ('bottom')
    elif top:
        horizontalTouch = abs(touching.width - (abs(touching.left - touched.left)))
        verticalTouch = abs(touching.height - (abs(touching.bottom - touched.bottom))) / 1.5
        if left and right:
            return ('top')
        elif left:
            
            if horizontalTouch > verticalTouch:
                return ('top')
            else:
                
                return ('left')
        elif right:
            if horizontalTouch > verticalTouch:
                return ('top')
            else:
                return ('right')
        else:
            return ('top')
    elif left:
        return ('left')
    elif right:
        return ('right')

    return None