//
//  YoIaKThjzxjghjweesrgklhse.m
//  DecodeTest
//
//  Created by Yimmm on 2020/2/26.
//  Copyright © 2020 alpha. All rights reserved.
//

#import "YoIaKThjzxjghjweesrgklhse.h"

@implementation YoIaKThjzxjghjweesrgklhse

// 处理double类型
+ (NSMutableDictionary *)YoIaKThjzxjghjweesrgklhseD22ubLHan:(double)myDou HTISEOIvhnnb:(NSString *)canshuStr HTISEbvio49hda:(double)canshuDou
{
//    NSLog(@"before --- %f",myDou);
    
    myDou = myDou + canshuDou + [canshuStr length];
    NSDictionary * myDic = @{[canshuStr uppercaseString] : @(myDou)};
    NSMutableDictionary * retMuDic = [NSMutableDictionary dictionaryWithDictionary:myDic];
    [retMuDic setObject:@(canshuDou) forKey:[canshuStr lowercaseString]];
    // 垃圾操作
    canshuStr = [retMuDic descriptionInStringsFileFormat];
    [retMuDic removeObjectsForKeys:@[canshuStr]];
    
    return retMuDic;
}

// 还原double类型
+ (double)YoIaKThjzxjghjweesrgklhseD22ubLRE:(NSMutableDictionary *)retMuDic
{
    double myDou = 2.0;
    NSArray * keysArr = [retMuDic allKeys];
    NSString * UPstr = [keysArr firstObject];
    if ([[UPstr lowercaseString]isEqualToString:[keysArr lastObject]])
    {
        myDou = myDou + [[retMuDic objectForKey:UPstr]doubleValue];
        myDou = myDou - [[retMuDic objectForKey:[UPstr lowercaseString]]doubleValue];
    }
    else
    {
        myDou = myDou + [[retMuDic objectForKey:[UPstr uppercaseString]]doubleValue];
        myDou = myDou - [[retMuDic objectForKey:UPstr]doubleValue];
    }
    myDou = myDou - [UPstr length] - [[retMuDic allValues]count];
    
//    NSLog(@"after ---  %f",myDou);
    return myDou;
    
}

// 处理long long类型
+ (NSMutableDictionary *)YoIaKThjzxjghjweesrgklhseLHongAN:(long long *)zhiLOng HDSVoirashb:(NSString *)canshuStr HGTIbre0943jkDNk:(NSUInteger)canUint
{
//    NSLog(@"before --- %lld",*zhiLOng);
    long long myLong = *zhiLOng + canUint + [canshuStr length];
    NSDictionary * myDic = @{[canshuStr uppercaseString] : @(myLong)};
    NSMutableDictionary * retMuDic = [NSMutableDictionary dictionaryWithDictionary:myDic];
    [retMuDic setObject:@(canUint) forKey:[canshuStr lowercaseString]];
    // 垃圾操作
    canshuStr = [retMuDic descriptionInStringsFileFormat];
    [retMuDic removeObjectsForKeys:@[canshuStr]];
    
    return retMuDic;
}

// 还原long long类型
+ (long long)YoIaKThjzxjghjweesrgklhseLHongRE:(NSMutableDictionary *)retMuDic
{
    //    double myDL = 0;
    long long myLong = 4;
    
    NSArray * keysArr = [retMuDic allKeys];
    NSString * UPstr = [keysArr firstObject];
    myLong = myLong - [keysArr count];
    if ([[UPstr lowercaseString]isEqualToString:[keysArr lastObject]])
    {
        myLong = myLong + [[retMuDic objectForKey:UPstr]longLongValue];
        myLong = myLong - [[retMuDic objectForKey:[UPstr lowercaseString]]longLongValue];
    }
    else
    {
        myLong = myLong + [[retMuDic objectForKey:[UPstr uppercaseString]]longLongValue];
        myLong = myLong - [[retMuDic objectForKey:UPstr]longLongValue];
    }
    myLong = myLong - [UPstr length] - [[retMuDic allValues]count];
    
//    NSLog(@"after ---  %lld",myLong);
    return myLong;
}

// 处理字符串
+ (NSArray *)YoIaKThjzxjghjweesrgklhseHNstigAn:(NSString **)cLStr Hiovanbreia:(NSString *)canshuStr HTIdavlirang98:(NSUInteger)Integ1  HTIreabv0943nlj:(NSUInteger)Integ2
{
    if (*cLStr == nil) {
        return nil;
    }
//    NSLog(@"before --- %@",*cLStr);
    if (*cLStr == NULL)
    {
        return @[@"Hy8FGg3h8Ghwe1gHwet"];
    }
    
    if (Integ1 == Integ2)
    {
        Integ1 = Integ1 + [*cLStr length] % 5;
    }
    
    NSMutableString * myMuStr = [[NSMutableString alloc]initWithString:*cLStr];
    if (Integ1 < [myMuStr length])
    {
        [myMuStr insertString:[NSString stringWithFormat:@"Integ%lu",(unsigned long)Integ1] atIndex:Integ1];
    }
    else
    {
        [myMuStr insertString:[NSString stringWithFormat:@"Integ%lu",(unsigned long)Integ1] atIndex:[myMuStr length]];
        
        // 垃圾操作
        canshuStr = [myMuStr stringByReplacingOccurrencesOfString:canshuStr withString:[canshuStr capitalizedString]];
    }
    
    if (Integ2 < [myMuStr length])
    {
        [myMuStr insertString:[NSString stringWithFormat:@"Integ%lu",(unsigned long)Integ2] atIndex:Integ2];
        
        // 垃圾操作
        canshuStr = [myMuStr stringByReplacingOccurrencesOfString:canshuStr withString:[canshuStr capitalizedString]];
    }
    else
    {
        [myMuStr insertString:[NSString stringWithFormat:@"Integ%lu",(unsigned long)Integ2] atIndex:[myMuStr length]];
    }
    NSArray * myArr = @[myMuStr,[NSString stringWithFormat:@"Integ%lu",(unsigned long)Integ1],[NSString stringWithFormat:@"Integ%lu",(unsigned long)Integ2]];
    
    //垃圾操作
    myArr = [myArr arrayByAddingObjectsFromArray:@[*cLStr, canshuStr]];
    //    myArr = [[myArr reverseObjectEnumerator]allObjects];
    //    Integ1 = Integ1 + [myMuStr length];
    //    Integ2 = Integ2 + [myArr count];
    
    return myArr;
}


// 还原字符串
+ (NSString *)YoIaKThjzxjghjweesrgklhseRNstigE:(NSArray *)myArr Hiovanbreia:(NSString *)canshuStr
{
    if (myArr == nil) {
        return nil;
    }
    //垃圾操作
    myArr = [myArr subarrayWithRange:NSMakeRange(0, [myArr count] - 2)];
    //    myArr = [[myArr reverseObjectEnumerator]allObjects];
    
    if ([myArr isEqualToArray:@[@"Hy8FGg3h8Ghwe1gHwet"]])
    {
        //        [myArr enumerateObjectsUsingBlock:^(id  _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop) {
        //        }];
        return nil;
    }
    
    NSString * midStr = [myArr firstObject];
    
    midStr = [midStr stringByReplacingOccurrencesOfString:[NSString stringWithFormat:@"%@",[myArr lastObject]] withString:@""];
    if (![midStr hasSuffix:[NSString stringWithFormat:@"%@",[myArr objectAtIndex:1]]])
    {
        midStr = [midStr stringByReplacingOccurrencesOfString:[NSString stringWithFormat:@"%@",[NSString stringWithFormat:@"%@",[myArr objectAtIndex:1]]] withString:@""];
        
        // 垃圾操作
        myArr = [myArr arrayByAddingObject:[canshuStr lowercaseString]];
    }
    else
    {
        // 垃圾操作
        myArr = [myArr arrayByAddingObject:[canshuStr lowercaseString]];
        
        midStr = [midStr substringToIndex:[midStr length] - [[NSString stringWithFormat:@"%@",[myArr objectAtIndex:1]]length]];
    }
    
    //垃圾操作
    midStr = [midStr stringByReplacingOccurrencesOfString:canshuStr withString:[myArr description]];
    
//    NSLog(@"after ---  %@",midStr);
    return midStr;
}

// 处理数组
+ (NSArray *)YoIaKThjzxjghjweesrgklhserRayHan:(NSArray **)changeArr HTIVlir93Ah2n44:(NSString *)canshuStr
{
//    NSLog(@"before --- %@",*changeArr);
    NSArray * midArr;
    
    *changeArr = [[*changeArr reverseObjectEnumerator]allObjects];
    
    if ([*changeArr count] % 2 == 0)
    {
        midArr = [NSArray arrayWithArray:[*changeArr subarrayWithRange:NSMakeRange([*changeArr count]/2, [*changeArr count]/2)]];
        midArr = [[midArr reverseObjectEnumerator]allObjects];
        
        // 垃圾操作
        canshuStr = [canshuStr capitalizedString];
        
        *changeArr = [*changeArr subarrayWithRange:NSMakeRange(0, [*changeArr count]/2)];
        *changeArr = [[*changeArr reverseObjectEnumerator]allObjects];
        midArr = [*changeArr arrayByAddingObjectsFromArray:midArr];
        
        //        垃圾操作
        midArr = [midArr arrayByAddingObject:canshuStr];
        
    }
    else
    {
        // 垃圾操作
        canshuStr = [canshuStr capitalizedString];
        
        *changeArr = [*changeArr arrayByAddingObject:[NSString stringWithFormat:@"ArrIsS1mple%@",canshuStr]];
        midArr = [NSArray arrayWithArray:[*changeArr subarrayWithRange:NSMakeRange([*changeArr count]/2, [*changeArr count]/2)]];
        midArr = [[midArr reverseObjectEnumerator]allObjects];
        
        *changeArr = [*changeArr subarrayWithRange:NSMakeRange(0, [*changeArr count]/2)];
        *changeArr = [[*changeArr reverseObjectEnumerator]allObjects];
        midArr = [*changeArr arrayByAddingObjectsFromArray:midArr];
        
        //垃圾操作
        *changeArr = [midArr subarrayWithRange:NSRangeFromString(canshuStr)];
    }
    
    return midArr;
}

// 还原数组
+ (NSArray *)YoIaKThjzxjghjweesrgklhseRErRay:(NSArray *)changeArr HTEAoviewnrgb:(NSString *)canshuStr
{
    NSArray * midArr;
    
    //    垃圾操作
    if ([changeArr count] % 2 != 0)
    {
        changeArr = [changeArr subarrayWithRange:NSMakeRange(0, [changeArr count] - 1)];
    }
    
    midArr = [NSArray arrayWithArray:[changeArr subarrayWithRange:NSMakeRange([changeArr count]/2, [changeArr count]/2)]];
    midArr = [[midArr reverseObjectEnumerator]allObjects];
    
    changeArr = [changeArr subarrayWithRange:NSMakeRange(0, [changeArr count]/2)];
    changeArr = [[changeArr reverseObjectEnumerator]allObjects];
    midArr = [changeArr arrayByAddingObjectsFromArray:midArr];
    
    // 垃圾操作
    canshuStr = [canshuStr decomposedStringWithCanonicalMapping];
    if ([changeArr containsObject:canshuStr])
    {
        changeArr = [midArr arrayByAddingObjectsFromArray:[canshuStr componentsSeparatedByString:[midArr description]]];
    }
    
    if ([[midArr lastObject]isKindOfClass:[NSString class]])
    {
        if ([[midArr lastObject]isEqualToString:@"ArrIsS1mple"])
        {
            midArr = [midArr subarrayWithRange:NSMakeRange(0, [midArr count]-1)];
        }
    }
    
    
    midArr = [[midArr reverseObjectEnumerator]allObjects];
    
//    NSLog(@"after ---  %@",midArr);
    return midArr;
}


@end
