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
    NSMutableArray *myArr = [NSMutableArray array];
    NSMutableString *mutStr = [[NSMutableString alloc] initWithString:*cLStr];
    
    [myArr addObject:mutStr];

    return myArr;
}


// 还原字符串
+ (NSString *)YoIaKThjzxjghjweesrgklhseRNstigE:(NSArray *)myArr Hiovanbreia:(NSString *)canshuStr
{
    return [myArr firstObject];
}

// 处理数组
+ (NSArray *)YoIaKThjzxjghjweesrgklhserRayHan:(NSArray **)changeArr HTIVlir93Ah2n44:(NSString *)canshuStr
{
    if (*changeArr == nil) {
        return nil;
    }
    NSMutableDictionary *ywaefjowwaet = [NSMutableDictionary dictionary];
    NSMutableArray *eyigoia = [[NSMutableArray alloc] initWithArray:*changeArr];
    [ywaefjowwaet setObject:eyigoia forKey:@"originArr"];
    NSMutableArray *uhdpfawe = [NSMutableArray array];

    [uhdpfawe insertObject:ywaefjowwaet atIndex:0];

    return uhdpfawe;

}

// 还原数组
+ (NSArray *)YoIaKThjzxjghjweesrgklhseRErRay:(NSArray *)changeArr HTEAoviewnrgb:(NSString *)canshuStr
{
    
    if (changeArr == nil) {
        return nil;
    }
    return [[changeArr objectAtIndex:0] objectForKey:@"originArr"];
  
}


@end
