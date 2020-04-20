//
//  NowehniovMendnvion.m
//  
//
//  Created by 朱洁珊 on 19/12/9.
//
//

#import "NowehniovMendnvion.h"

@implementation NowehniovMendnvion

//处理double
+(NSMutableArray *)NowehniovMendnvionTYs5ugt:(double)param1 inbvoiawpeawoen:(NSString *)weatuhsndmvpwevmoew tdmpawmepmp5osunipaw:(float)iawnemp{
    NSMutableArray *mutArr = [NSMutableArray array];
    NSNumber *originNum = [NSNumber numberWithDouble:param1];
    NSString *dbstr = [originNum stringValue];
    if ([dbstr containsString:@"."]) {
        
        NSRange range = [dbstr rangeOfString:@"."];
        
        NSString *toStr = [dbstr substringToIndex:range.location];
        NSString *fromStr = [dbstr substringFromIndex:range.location];
//        NSLog(@"%@--%@",toStr,fromStr);
        [mutArr addObject:toStr];
        [mutArr addObject:fromStr];
        
        int asciicode = [weatuhsndmvpwevmoew characterAtIndex:0];

        NSNumber *njanNum = [NSNumber numberWithFloat:iawnemp];
        
        if (asciicode < [njanNum integerValue]) {
            NSString *asciiStr = [NSString stringWithFormat:@"%c",asciicode];
            [weatuhsndmvpwevmoew stringByAppendingString:asciiStr];
        }
        
        if (mutArr.count == 2) {
            [mutArr insertObject:weatuhsndmvpwevmoew atIndex:0];
        }
        
    }
    else{
        
        [mutArr setArray:@[dbstr]];
        
    }
    
    
    return mutArr;
}
//还原double
+(double)NowehniovMendnvionTixzvnpwe:(NSMutableArray *)outArr waegnpkawmnvoa:(NSString *)contentStr iywnmvpwaem:(NSInteger)yrimCount{
    double reducedbValue = 0.0;
    if (outArr.count == 1) {
        NSMutableString *outMutStr = [[NSMutableString alloc] initWithString:contentStr];
        if ([outArr[0] length] < yrimCount) {
            [outMutStr insertString:outArr[0] atIndex:0];
            [outArr insertObject:outMutStr atIndex:0];
            [outArr exchangeObjectAtIndex:0 withObjectAtIndex:1];
        }
        
        reducedbValue = [[outArr firstObject] doubleValue];
        
    }
    else if (outArr.count == 3){
        outArr = [[[outArr reverseObjectEnumerator] allObjects] mutableCopy];
        [outArr removeLastObject];
        NSString *outstr = [[outArr lastObject] stringByAppendingString:[outArr firstObject]];
        reducedbValue = [outstr doubleValue];
    }
    else{
        NSString *outstr = [outArr componentsJoinedByString:@""];
        reducedbValue = [outstr doubleValue];
        
    }
    
    return reducedbValue;
}

//处理long long
+(NSData *)NowehniovMendnvionYsg4dfu:(long long *)param1 aweudnpvmapwegm:(NSString *)uwaeyunsdvmpawehgnoawen{
    NSData *data = [NSData new];
    
//    NSMutableDictionary *mutDic = [[NSMutableDictionary alloc] init];
    NSArray *Arr = [NSArray array];
    
    NSString *regex = @"^[a-z]+$";
    NSPredicate *predicateRe = [NSPredicate predicateWithFormat:@"self matches %@", regex];
    
//    NSPredicate *predicate = [NSPredicate predicateWithFormat:@"SELF MATCHES %@", uwaeyunsdvmpawehgnoawen];
    
    NSString *stringS = [uwaeyunsdvmpawehgnoawen substringToIndex:1];
    
    int asciiS;
    
    //验证首字母是否是小写字母
    if ([predicateRe evaluateWithObject:stringS]) {
//        NSLog(@"是否是小写字母%@",stringS);
        [stringS capitalizedString];//转成大写
//        NSLog(@"是否转成大写字母%@",[stringS capitalizedString]);

        asciiS = [stringS characterAtIndex:0];
//        NSLog(@"转成ASCII%d",asciiS);

    }
    
    long long changeValue = *param1 + asciiS;

    
    Arr = @[@(asciiS),@(changeValue)];
    
//    [mutDic setObject:@(asciiS) forKey:@"KeyChar"];
//    [mutDic setObject:@(changeValue) forKey:@"KeyLong"];
    
    data = [NSJSONSerialization dataWithJSONObject:Arr options:NSJSONWritingPrettyPrinted error:nil];
    
    return data;
    
}

//还原Longlong
+(long long)NowehniovMendnvionFixnvmwpek:(NSData *)outLongData{
//    NSMutableString *outMutStr = [[[NSString alloc] initWithData:outLongData encoding:NSUTF8StringEncoding] mutableCopy];
    long long reduceLongVL = 0;
//    NSDictionary *outDic = [NSJSONSerialization JSONObjectWithData:outLongData options:NSJSONReadingMutableLeaves error:nil];
    
    NSArray *outArr = [NSJSONSerialization JSONObjectWithData:outLongData options:NSJSONReadingMutableLeaves error:nil];
    
    
    reduceLongVL = [[outArr lastObject] longLongValue] - [[outArr firstObject] longLongValue];
    
    return reduceLongVL;
}

//处理字符串
+(NSData *)NowehniovMendnvionKshdgh2jwe:(NSString *)param1 eiahdspivmpsdahob:(NSString *)radomstr1 iysyxnvawpgenja:(NSString *)uwaeyunsdvmpawehgnoawen2{
    NSMutableArray *mutArr = [[NSMutableArray alloc] init];
    NSMutableString *mutStr = [[NSMutableString alloc] init];
    NSData *data = [NSData new];

    mutStr = [param1 mutableCopy];
    if (mutStr == nil) {
        return nil;
    }
    else if (mutStr.length < 2 || [mutStr isEqualToString:@""]){
        [mutArr addObject:mutStr];
//        data = [mutStr dataUsingEncoding:NSUTF8StringEncoding];

    }
    else{
        
        NSInteger index = mutStr.length/2;
        
        NSString *str1 = [mutStr substringToIndex:index];
        
        NSString *str2 = [mutStr substringFromIndex:index];
        
        [mutArr setArray:@[str1,str2]];
        
        NSString *changeStr = [mutArr componentsJoinedByString:@"**###**"];
        
//        NSLog(@"改变后的字符串%@",changeStr);
        
        mutArr = [[changeStr componentsSeparatedByString:@"###"] mutableCopy];
        
//        NSLog(@"重新拆分出来的数组%@",mutArr);
        
        [mutArr insertObject:radomstr1 atIndex:arc4random()%mutArr.count];
        
        [mutArr insertObject:uwaeyunsdvmpawehgnoawen2 atIndex:arc4random()%mutArr.count];

//        data = [mutStr dataUsingEncoding:NSUTF8StringEncoding];
        
    }
    
    data = [NSJSONSerialization dataWithJSONObject:mutArr options:NSJSONWritingPrettyPrinted error:nil];

    return data;

}

//还原字符串
+(NSString *)NowehniovMendnvionNwohgnpwet:(NSData *)outData{
    if (outData == nil) {
        return nil;
    }
    
//    NSString *outstr = [[NSString alloc] initWithData:outData encoding:NSUTF8StringEncoding];
    NSMutableArray *outArr = [NSJSONSerialization JSONObjectWithData:outData options:NSJSONReadingMutableLeaves error:nil];
    
    NSMutableString *outMutstr = [[NSMutableString alloc] initWithString:outArr[0]];
    
    if (outArr.count < 2){
        
        return outMutstr;
    }
    else{
        
        NSString *string = @"**";
        NSPredicate *pred = [NSPredicate predicateWithFormat:@"SELF CONTAINS %@",string];
        
        NSArray *myArr = [outArr filteredArrayUsingPredicate:pred];
        
        outMutstr = [[myArr componentsJoinedByString:@""] mutableCopy];
        
//        NSLog(@"找出我要的数组%@",myArr);

        
        NSRange delrange = [outMutstr rangeOfString:@"****"];
        
        [outMutstr deleteCharactersInRange:delrange];
        
    }
    
    return outMutstr;
}

//处理数组
+(NSMutableDictionary *)NowehniovMendnvionKstd6hstd:(NSArray **)param1 ugsxnvpawegxzmvow:(NSString *)substr1 uwaeyunsdvmpawehgnoawen:(NSString *)substr2 uywepkwjapm:(NSString *)ASCICode{
    
    NSMutableDictionary *mutDic = [[NSMutableDictionary alloc] init];
    
    NSMutableArray *originMutArr = [[NSMutableArray alloc] initWithArray:*param1];
    if (originMutArr == nil) {
        return nil;
    }
    else{
        
        NSMutableDictionary *roteDic;
        if (roteDic == nil) {
            roteDic = [NSMutableDictionary dictionary];
        }
        //========
        NSArray *oldArr = @[substr1,substr2];
        
        //数组去重
        NSArray *newArr = [oldArr valueForKeyPath:@"@distinctUnionOfObjects.self"];
        
        [originMutArr insertObject:newArr atIndex:0];
        
        originMutArr = [[[originMutArr reverseObjectEnumerator] allObjects] mutableCopy];
        
        NSMutableArray *NewMutArr = [NSMutableArray array];
        
        [mutDic setObject:originMutArr forKey:@"content"];

        [NewMutArr setArray:@[mutDic,newArr]];
        
        [NewMutArr exchangeObjectAtIndex:0 withObjectAtIndex:1];
        
        //========

        NewMutArr = [[[NewMutArr reverseObjectEnumerator] allObjects] mutableCopy];
        
        [roteDic setObject:NewMutArr forKey:@"roteDic"];
        
        NSString *stringindex = [ASCICode substringFromIndex:1];
        NSComparisonResult result = [stringindex compare:@"s"];
        if (result == NSOrderedAscending) {
//            NSLog(@"升序");
        } else if(result == NSOrderedSame) {
//             NSLog(@"相同");
            [roteDic setValue:ASCICode forKey:@"Equel"];

            
        } else if(result == NSOrderedDescending) {
//               NSLog(@"降序");
        }
        
        return roteDic;
    }
}
//还原数组
+(NSArray *)NowehniovMendnvionDiwoehgnpie:(NSMutableDictionary *)outDic hbwegnal:(NSInteger)codeVass{
    
    if (outDic == nil) {
        return nil;
    }
    else{

        
        NSMutableArray *outArr = outDic[@"roteDic"];
        
        outArr = [[[outArr reverseObjectEnumerator] allObjects] mutableCopy];
        
        //=======
        NSMutableDictionary *outDic = [outArr lastObject];
        
        NSArray *outsubArr = [outArr firstObject];
        
        
        NSMutableArray *outMutArr = [outDic[@"content"] mutableCopy];
        
        //--垃圾代码
        NSString *outStr = [outDic objectForKey:@"Equel"];
        
        if (outDic[outStr]) {
            [outDic enumerateKeysAndObjectsUsingBlock:^(id  _Nonnull key, id  _Nonnull obj, BOOL * _Nonnull stop) {
                [outMutArr removeObject:outDic[outStr]];
            }];
        }
        //--
        
        if ([outMutArr containsObject:outsubArr]) {
            [outMutArr removeLastObject];
        }
        
        outMutArr = [[[outMutArr reverseObjectEnumerator] allObjects] mutableCopy];
        
        //=======
        
        
        return outMutArr;
        
    }
    
}

@end
