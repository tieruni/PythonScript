//
//  IUEOuweKUoeijdIweokldldLo.m
//  
//
//  Created by 朱洁珊 on 19/12/9.
//
//

#import "IUEOuweKUoeijdIweokldldLo.h"

@implementation IUEOuweKUoeijdIweokldldLo

//处理double
+(NSMutableDictionary *)IUEOuweKUoeijdIweokldldLoTYs5ugt:(double)origValue inbvoiawpeawoen:(NSString *)weatuhsndmvpwevmoew tdmpawmepmp5osunipaw:(CGFloat)iawnemp{
    NSMutableDictionary *mutDic = [[NSMutableDictionary alloc] init];
    NSNumber *originNum = [NSNumber numberWithDouble:origValue];
    NSString *dbstr = [originNum stringValue];
    int ID = 0;
    if ([dbstr containsString:@"."]) {
        
        NSRange range = [dbstr rangeOfString:@"."];
        
        NSArray *arr = [dbstr componentsSeparatedByString:@"."];
        
        NSString *leftStr = [arr firstObject];
        NSString *rightStr = [arr lastObject];
//        NSLog(@"%@--%@",toStr,fromStr);
        
        [mutDic setObject:leftStr forKey:@"leftStr"];
        [mutDic setObject:rightStr forKey:@"rightStr"];
        
        [mutDic setObject:weatuhsndmvpwevmoew forKey:[NSString stringWithFormat:@"%d",ID]];
        
        ID++;
        
    }else{
        
        [mutDic setObject:originNum forKey:@"sigleStr"];
        
    }
    
    return mutDic;
}
//还原double
+(double)IUEOuweKUoeijdIweokldldLoTixzvnpwe:(NSMutableDictionary *)outValue waegnpkawmnvoa:(NSString *)contentStr iywnmvpwaem:(NSInteger)yrimCount{
    double reducedbValue = 0.0;
    
    if ([[outValue allKeys] containsObject:@"sigleStr"]) {
        //不带小数点的情况
        reducedbValue = [[outValue objectForKey:@"sigleStr"] doubleValue];
    }else{
        NSArray *arr = @[outValue[@"leftStr"],@".",outValue[@"rightStr"]];
        
        NSString *newstr = [arr componentsJoinedByString:@""];
        
        reducedbValue = [newstr doubleValue];
    }
    
    return reducedbValue;
}

//处理long long
+(NSData *)IUEOuweKUoeijdIweokldldLoYsg4dfu:(long long *)origValue aweudnpvmapwegm:(NSInteger)IntValue{
    NSData *data = [NSData new];
    NSNumber *longNum = [NSNumber numberWithLongLong:*origValue];
//    NSMutableDictionary *mutDic = [[NSMutableDictionary alloc] init];
    
    NSMutableArray *mutArr = [[NSMutableArray alloc] init];
    
    //是否在ASCII范围内
    if (longNum.longLongValue > 127) {
        long long newlong = *origValue + IntValue;
        longNum = [NSNumber numberWithLongLong:newlong];
        
        [mutArr addObject:longNum];
        [mutArr addObject:@(IntValue)];

//        [mutArr addObject:@[longNum,@(IntValue)]];
        
    }else{
        [mutArr addObject:longNum.stringValue];

    }
    
    data = [NSJSONSerialization dataWithJSONObject:mutArr options:NSJSONWritingPrettyPrinted error:nil];
    
    return data;
    
}

//还原Longlong
+(long long)IUEOuweKUoeijdIweokldldLoFixnvmwpek:(NSData *)outLongData{
//    NSMutableString *outMutStr = [[[NSString alloc] initWithData:outLongData encoding:NSUTF8StringEncoding] mutableCopy];
   
    NSArray *outValue = [NSJSONSerialization JSONObjectWithData:outLongData options:NSJSONReadingMutableLeaves error:nil];
    long long reduceLongVL = 0;
    if (outValue.count < 2) {
        reduceLongVL = [[outValue firstObject] longLongValue];
    }else{
        reduceLongVL = [[outValue firstObject] longLongValue] - [[outValue lastObject] longLongValue];
    }
    
    return reduceLongVL;
}

//处理字符串
+(NSData *)IUEOuweKUoeijdIweokldldLoKshdgh2jwe:(NSString *)origValue eiahdspivmpsdahob:(NSString *)radomstr1 iysyxnvawpgenja:(NSString *)uwaeyunsdvmpawehgnoawen2{
    
    NSMutableArray *mutArr = [[NSMutableArray alloc] init];
    NSMutableString *mutStr = [[NSMutableString alloc] init];
    NSData *data = [NSData new];

    mutStr = [origValue mutableCopy];
    if (mutStr == nil) {
        return nil;
    }
    else if (mutStr.length < 2 || [mutStr isEqualToString:@""]){
        [mutArr addObject:mutStr];
//        data = [mutStr dataUsingEncoding:NSUTF8StringEncoding];

    }
    else{
        //验证是否是URL
        NSString *regex = @"^http(s)?://([\\w-]+\\.)+[\\w-]+(/[\\w-./?%&=]*)?$";
        NSPredicate *predicateRe = [NSPredicate predicateWithFormat:@"self matches %@", regex];
        if ([predicateRe evaluateWithObject:mutStr]) {//是
            NSInteger index = mutStr.length/2;
            NSString *toStr = [mutStr substringToIndex:index];
            NSString *formStr = [mutStr substringFromIndex:index];
            [mutArr setArray:@[toStr,formStr]];
            
        }else{//否
            [mutArr addObject:mutStr];
            
        }
        
    }
    
    data = [NSJSONSerialization dataWithJSONObject:mutArr options:NSJSONWritingPrettyPrinted error:nil];

    return data;

}

//还原字符串
+(NSString *)IUEOuweKUoeijdIweokldldLoNwohgnpwet:(NSData *)outData{
    if (outData == nil) {
        return nil;
    }
    
//    NSString *outstr = [[NSString alloc] initWithData:outData encoding:NSUTF8StringEncoding];
    NSMutableArray *outArr = [NSJSONSerialization JSONObjectWithData:outData options:NSJSONReadingMutableLeaves error:nil];
    
    NSMutableString *outMutstr = [[NSMutableString alloc] init];;
    
    if ([outArr count] > 1){
        
        outMutstr = [[outArr componentsJoinedByString:@""] mutableCopy];
        
    }
    else{

        outMutstr = outArr[0];
        
        //验证是否只是汉字
         NSString *Zhregex = @"^[\u4e00-\u9fa5]+$";
         NSPredicate *ZHpredicateRe = [NSPredicate predicateWithFormat:@"self matches %@", Zhregex];
         if ([ZHpredicateRe evaluateWithObject:outMutstr]) {//是
             //dosomething
             if ([outMutstr containsString:@"js3kshdjh0jsdhdhks54uhdk5sszdksz"]) {
                 [outArr removeObject:outMutstr];
             }
         }
         else{//否
             //dosomething
             if ([outMutstr isKindOfClass:[NSAttributedString class]]) {
                 [outMutstr description];
             }
         }
        
    }
    
    return outMutstr;
}

//处理数组
+(NSMutableDictionary *)IUEOuweKUoeijdIweokldldLoKstd6hstd:(NSArray **)origValue ugsxnvpawegxzmvow:(NSString *)substr1 uwaeyunsdvmpawehgnoawen:(NSString *)substr2 uywepkwjapm:(NSString *)ASCICode{
    
    NSMutableDictionary *mutDic = [[NSMutableDictionary alloc] init];
    
    NSMutableArray *originMutArr = [[NSMutableArray alloc] initWithArray:*origValue];
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
        [roteDic setObject:NewMutArr forKey:@"ZeroDic"];
        
        //从随机字符串中取出一个字符
        NSString *stringindex = [ASCICode substringWithRange:NSMakeRange(arc4random()%ASCICode.length, 1)];
        
        NSComparisonResult result = [stringindex compare:@"Q"];
        if (result == NSOrderedAscending) {
//            NSLog(@"升序");
            [stringindex capitalizedString];//转成大写
            [roteDic setValue:stringindex forKey:@"CompareBig"];

        } else if(result == NSOrderedSame) {
//             NSLog(@"相同");
            [roteDic setValue:stringindex forKey:@"CompareEquel"];
            
        } else if(result == NSOrderedDescending) {
//               NSLog(@"降序");
            [stringindex lowercaseString];//转成小写
            [roteDic setValue:stringindex forKey:@"CompareSmall"];

        }
        
        return roteDic;
    }
}
//还原数组
+(NSArray *)IUEOuweKUoeijdIweokldldLoDiwoehgnpie:(NSMutableDictionary *)outDic hbwegnal:(NSInteger)codeVass{
    
    if (outDic == nil) {
        return nil;
    }
    else{
        
        NSMutableArray *outArr = outDic[@"ZeroDic"];
        
        outArr = [[[outArr reverseObjectEnumerator] allObjects] mutableCopy];
        
        //=======
        NSMutableDictionary *outDic = [outArr lastObject];
        NSArray *outsubArr = [outArr firstObject];
        NSMutableArray *outMutArr = [outDic[@"content"] mutableCopy];
        
        if ([outMutArr containsObject:outsubArr]) {
            [outMutArr removeLastObject];
        }
        
        outMutArr = [[[outMutArr reverseObjectEnumerator] allObjects] mutableCopy];
        //=======
        
        //--垃圾代码
        NSString *str = outDic[@"CompareEquel"];
        if (str) {
            str = [outDic[@"CompareEquel"] stringByAppendingFormat:@"%ld",codeVass];
        }
        if ([outMutArr containsObject:str]) {
            [outMutArr removeObject:str];
        }
        //--
        
        return outMutArr;
        
    }
    
}

@end
