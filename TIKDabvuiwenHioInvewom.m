//
//  TIKDabvuiwenHioInvewom.m
//  DecodeTest
//
//  Created by Yimmm on 2020/2/11.
//  Copyright © 2020 alpha. All rights reserved.
//

#import "TIKDabvuiwenHioInvewom.h"

@implementation TIKDabvuiwenHioInvewom


// 处理double类型
+ (NSMutableArray *)TIKDabvuiwenHioInvewomHADuolebN:(double)myDou NowWeSeen:(NSString *)canshuStr
{
//        NSLog(@"before --- %f",myDou);
    NSString * douStr = [NSString stringWithFormat:@"%f",myDou + [canshuStr length]];
    
    NSMutableArray * myMuArr = [NSMutableArray arrayWithArray:[douStr componentsSeparatedByString:@"."]];
    
    //垃圾操作
    douStr = [douStr stringByAppendingPathExtension:canshuStr];
    [myMuArr removeObject:douStr];
    
    if ([[myMuArr firstObject]hasSuffix:@"0"])
    {
        [myMuArr replaceObjectAtIndex:0 withObject:[NSString stringWithFormat:@"%@",[[myMuArr firstObject]substringToIndex:[[myMuArr firstObject]length]-1]]];
        [myMuArr replaceObjectAtIndex:1 withObject:[NSString stringWithFormat:@"0%@",[myMuArr lastObject]]];
    }
    else
    {
        [myMuArr replaceObjectAtIndex:1 withObject:[NSString stringWithFormat:@"%@DSB35",[myMuArr lastObject]]];
    }
    
    // 垃圾操作
    [myMuArr insertObject:canshuStr atIndex:[myMuArr count]];
    
    return myMuArr;
}

// 还原double类型
+ (double)TIKDabvuiwenHioInvewomREDuoleb0:(NSMutableArray *)myMuArr NowWeSeen:(NSString *)canshuStr
{
    double myDou = 0.0;
    // 垃圾操作
    myDou = myDou + [canshuStr length];
    canshuStr = [canshuStr stringByReplacingOccurrencesOfString:canshuStr withString:[myMuArr lastObject]];
    [myMuArr removeLastObject];
    
    if ([[myMuArr lastObject]hasSuffix:@"DSB35"])
    {
        [myMuArr addObject:[[myMuArr lastObject]stringByReplacingOccurrencesOfString:@"DSB35" withString:@""]];
        [myMuArr removeObjectAtIndex:1];
        NSString * midStr = [myMuArr componentsJoinedByString:@"."];

        myDou = [midStr doubleValue];
    }
    else
    {
        NSString * midStr = [myMuArr componentsJoinedByString:@"."];
        if (![midStr isEqualToString:canshuStr])
        {
            myDou = [midStr doubleValue] * 10;
        }
    }
    myDou = myDou - [canshuStr length];

//        NSLog(@"after ---  %f",myDou);
    return myDou;
    
}

// 处理long long类型
+ (NSArray *)TIKDabvuiwenHioInvewomLionHaL0N:(long long *)zhiLOng SYUYSlwinfhWA8n:(NSString *)canshuStr
{
    NSNumber *longNUm = [NSNumber numberWithLongLong:*zhiLOng];
    
    NSMutableString *longStr = [[longNUm stringValue] mutableCopy];
    
    [longStr stringByAppendingFormat:@"**%@",longStr];
    
    NSMutableArray *outArr = [NSMutableArray array];
    
    [outArr addObject:longStr];
    
    return outArr;
}

// 还原long long类型
+ (long long)TIKDabvuiwenHioInvewomLionREL0N:(NSArray *)myMuArr
{
    long long myLong = 0;
    
    NSString *outStr = [myMuArr lastObject];
    
    myMuArr = [outStr componentsSeparatedByString:@"**"];
    
    int index = arc4random()%myMuArr.count;
    
    myLong = [myMuArr[index] longLongValue];
    
    return myLong;
}


// 处理字符串
+ (NSDictionary *)TIKDabvuiwenHioInvewomHAGTRSrNGN:(NSString **)cLStr SYUYSHNeverNever:(BOOL)mySwitch
{
//        NSLog(@"before --- %@",*cLStr);
    if (*cLStr == nil || [*cLStr isEqualToString:@""])
    {
        *cLStr = @"nilSttttr~";
    }
    NSMutableString * midStr = [[NSMutableString alloc]initWithString:*cLStr];
    NSDictionary * myDic;
    
    [midStr appendString:midStr];
    [midStr deleteCharactersInRange:NSMakeRange([midStr length] - 1, 1)];
    if (mySwitch)
    {
        myDic = @{midStr : @(0)};
    }
    else
    {
        myDic = @{@(0) : midStr};
    }
    
    return myDic;
}


// 还原字符串
+ (NSString *)TIKDabvuiwenHioInvewomREGTRSrNG0:(NSDictionary *)myDic
{
    NSMutableString * midStr;
    if ([[[myDic keyEnumerator]nextObject]isKindOfClass:[NSString class]])
    {
        midStr = [[myDic allKeys]firstObject];
    }
    else
    {
        midStr = [myDic objectForKey:@(0)];
    }
    if ([midStr containsString:@"nilSttttr~"])
    {
        return nil;
    }
//    [midStr deleteCharactersInRange:NSMakeRange([midStr length]/2 + 1, [midStr length]/2)];
    NSString * retstr = [midStr stringByAppendingString:@"8"];
    retstr = [midStr substringWithRange:NSMakeRange(0, [midStr length]/2 + 1)];
    
//        NSLog(@"after ---  %@",retstr);
    return retstr;
}


// 处理数组
+ (NSDictionary *)TIKDabvuiwenHioInvewomHAHARrrNAdren:(NSArray **)changeArr SSYTEhreu345k:(BOOL)onBool
{
//        NSLog(@"before --- %@",*changeArr);
    NSArray * midArr = *changeArr;
    NSMutableArray * myMuArr = [NSMutableArray arrayWithArray:midArr];
    [myMuArr addObjectsFromArray:*changeArr];
    NSDictionary * myDic;
    
    [myMuArr removeLastObject];
    if (onBool)
    {
        myDic = @{myMuArr : @(1)};
    }
    else
    {
        myDic = @{@(1) : myMuArr};
    }
    
    return myDic;
}

// 还原数组
+ (NSArray *)TIKDabvuiwenHioInvewomRE0HARrrNAdren:(NSDictionary *)myDic
{
    NSArray * myMuArr = [[NSArray alloc]init];
    if (![[[myDic keyEnumerator]nextObject]isKindOfClass:[NSNumber class]])
    {
        myMuArr = [[myDic allKeys]firstObject];
    }
    else
    {
        myMuArr = [[myDic allValues]firstObject];
    }
    myMuArr = [myMuArr arrayByAddingObject:@(1)];
//    [myMuArr addObject:@(1)];
//    [myMuArr removeObjectsInRange:NSMakeRange([myMuArr count]/2, [myMuArr count]/2)];
    myMuArr = [myMuArr subarrayWithRange:NSMakeRange(0, [myMuArr count]/2)];
    
//        NSLog(@"after ---  %@",myMuArr);
    return myMuArr;
}







@end
