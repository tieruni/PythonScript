//
//  UisgdiweeruIK.m
//  
//
//  Created by 朱洁珊 on 19/12/9.
//
//

#import "UisgdiweeruIK.h"

@implementation UisgdiweeruIK

//处理double
+(NSMutableArray *)UisgdiweeruIKTYs5ugt:(double)param1 yierhgiuhs:(NSString *)uaewbgojsrdt{
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
    }
    else{
        [mutArr setArray:@[dbstr]];
    }
    return mutArr;
}
//还原double
+(double)UisgdiweeruIKEJbd3sojgn:(NSMutableArray *)outArr{
    double reducedbValue = 0.0;
    if (outArr.count == 1) {
        reducedbValue = [outArr[0] doubleValue];
        return reducedbValue;
    }
    else{
        NSString *outstr = [outArr componentsJoinedByString:@""];
        reducedbValue = [outstr doubleValue];
    }
    
    return reducedbValue;
}

//处理long long
+(NSData *)UisgdiweeruIKYsg4dfu:(long long)param1 Tusdg3erhi:(NSString *)randomStr{
    NSData *data = [NSData new];
    NSMutableString *longMutStr = [NSMutableString new];
    NSNumber *originNum = [NSNumber numberWithLongLong:param1];
    NSString *longstr = [originNum stringValue];
//    if (*param1 = NULL) {
//        return NULL;
//    }
    if (longstr.length == 1) {
        data = [longstr dataUsingEncoding:NSUTF8StringEncoding];
    }
    else if (longstr.length == 2){
        longMutStr = [longstr mutableCopy];
        [longMutStr insertString:@"#" atIndex:longstr.length-1];
        data = [longMutStr dataUsingEncoding:NSUTF8StringEncoding];

    }else{
        longMutStr = [longstr mutableCopy];
        int randomInt = arc4random()%88;
        if (randomInt < 40) {
            [longMutStr insertString:[NSString stringWithFormat:@"%@++",randomStr] atIndex:0];
        }else{
            [longMutStr appendString:[NSString stringWithFormat:@"++%@",randomStr]];
        }
        data = [longMutStr dataUsingEncoding:NSUTF8StringEncoding];
    }
    
    
    return data;
}
//还原Longlong
+(long long)UisgdiweeruIKRdsbh9gierh:(NSData *)outLongData{
    NSMutableString *outMutStr = [[[NSString alloc] initWithData:outLongData encoding:NSUTF8StringEncoding] mutableCopy];
    long long reduceLongVL = 0;
//    if (outLongData = NULL) {
//        return NULL;
//    }
    if (outMutStr.length == 1) {
        reduceLongVL = [outMutStr longLongValue];
    }
    else if (outMutStr.length == 3 && [outMutStr containsString:@"#"]){
        NSArray *outArr = [outMutStr componentsSeparatedByString:@"#"];
        outMutStr = [[NSString stringWithFormat:@"%@%@",outArr[0],outArr[1]] mutableCopy];
        reduceLongVL = [outMutStr longLongValue];
    }
    else{
        if ([outMutStr containsString:@"++"]) {
            NSArray *outArr = [outMutStr componentsSeparatedByString:@"++"];
            NSString *firstStr = [NSString stringWithFormat:@"%@",outArr[0]];
            NSString *lastStr = [NSString stringWithFormat:@"%@",outArr[1]];
            if (firstStr.length > lastStr.length) {
                reduceLongVL = [lastStr longLongValue];
            }else{
                reduceLongVL = [firstStr longLongValue];
            }
        }
    }
    return reduceLongVL;
}

//处理字符串
+(NSData *)UisgdiweeruIKKshdgh2jwe:(NSString *)param1 hgvsghsdert:(NSString *)radomstr1 asghgbfiwjeg:(NSString *)randomstr2{
    NSMutableString *mutStr = [[NSMutableString alloc] init];
    NSData *data = [NSData new];

    mutStr = [param1 mutableCopy];
    if (mutStr == nil) {
        return nil;
    }
    else if (mutStr.length == 0 || [mutStr isEqualToString:@""]){
        data = [mutStr dataUsingEncoding:NSUTF8StringEncoding];
        return data;
    }
    else{
        int randomInterger = arc4random()%mutStr.length;
        [mutStr insertString:@"~~~~~" atIndex:randomInterger];
        data = [mutStr dataUsingEncoding:NSUTF8StringEncoding];
        return data;
    }
}
//还原字符串
+(NSString *)UisgdiweeruIKLysd7fudhk:(NSData *)outData{
    NSString *outstr = [[NSString alloc] initWithData:outData encoding:NSUTF8StringEncoding];
    NSMutableString *outMutstr = [outstr mutableCopy];
    if (outData == nil) {
        return nil;
    }
    else if (outMutstr.length == 0 || [outMutstr isEqualToString:@""]){
        
        return outMutstr;
    }
    else{
        NSRange range = [outMutstr rangeOfString:@"~~~~~"];
        NSString *toStr = [outMutstr substringToIndex:range.location];
        NSString *fromStr = [outMutstr substringFromIndex:range.location+@"~~~~~".length];
        outMutstr = [[toStr stringByAppendingString:fromStr] mutableCopy];
    }
    return outMutstr;
}

//处理数组
+(NSMutableDictionary *)UisgdiweeruIKKstd6hstd:(NSArray **)param1 title:(NSString *)substr1 color:(UIColor *)subcolor randomStr:(NSString *)randomstr{
    NSMutableDictionary *mutDic = [[NSMutableDictionary alloc] init];
    NSMutableArray *originMutArr = [[NSMutableArray alloc] initWithArray:*param1];
    if (originMutArr == nil) {
        return nil;
    }
    else if (originMutArr.count == 0 /*|| [originMutArr[0] isEqualToString:@""]*/){
//        NSString *outStr = [NSString stringWithFormat:@"%@",originMutArr[0]];
        [mutDic setObject:originMutArr forKey:@"null"];
        return mutDic;
    }
    else{
        [originMutArr insertObject:@"uyfbgiser" atIndex:0];
        originMutArr = [[[originMutArr reverseObjectEnumerator] allObjects] mutableCopy];
        [mutDic setObject:originMutArr forKey:@"content"];
        return mutDic;
    }
}
//还原数组
+(NSArray *)UisgdiweeruIKEtjdfb5hid:(NSMutableDictionary *)outDic{
    
    if (outDic == nil) {
        return nil;
    }
    else if (outDic[@"null"]){
        return outDic[@"null"];
    }
    else{
        NSMutableArray *outMutArr = [outDic[@"content"] mutableCopy];
        [outMutArr removeLastObject];
        outMutArr = [[[outMutArr reverseObjectEnumerator] allObjects] mutableCopy];
        return outMutArr;
    }
}

@end
