def trap(h):
  if not h:
    return 0

  l,r=0 ,len(h)-1
  left_max,right_max=h[l],h[r]
  res=0

  while l<r:
    if left_max<right_max:
      l+=1
      left_max=max(left_max,h[l])
      res+=left_max-h[l]

    else:
      r-=1
      right_max=max(right_max,h[r])
      res+=right_max-h[r]

  return res

trap([0,2,0,2,0])