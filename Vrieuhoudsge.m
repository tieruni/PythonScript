//
//  Vrieuhoudsge.m
//  
//
//  Created by 朱洁珊 on 19/12/9.
//
//

#import "Vrieuhoudsge.h"

//@interface Vrieuhoudsge()
//@property(strong , nonatomic)UILabel *sherlabel;
//
//@end

@implementation Vrieuhoudsge

//+(instancetype)sharesingleFunc{
//    static singletion *
//}

+ (UILabel *)shareManegerSingletion {
    static UILabel *_shareLabel = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{

        _shareLabel = [[UILabel alloc] init];
        
    });
    return _shareLabel;
}

//处理double
+(NSMutableArray *)VrieuhoudsgeTYs5ugt:(double)param1 yierhgiuhs:(NSString *)prefixStr uybUbuowrsd:(NSString *)sufixStr{
    
    NSMutableArray *mutArr = [NSMutableArray array];
    NSNumber *originNum = [NSNumber numberWithDouble:param1];
    NSString *dbstr = [originNum stringValue];

    if (![dbstr containsString:@"."] || [dbstr containsString:@".0"]) {
        [mutArr addObject:dbstr];
    }
    else{
        
        mutArr = [[dbstr componentsSeparatedByString:@"."] mutableCopy];
        
        CGPoint dbpoint = CGPointMake([mutArr[0] intValue], [mutArr[1] intValue]);
        
        UILabel *mylabrl = [self shareManegerSingletion];

        mylabrl.center = dbpoint;
        
        [mutArr setArray:@[mylabrl]];
        
    }
    
    return mutArr;
}

//还原double
+(double)VrieuhoudsgeEJbd3sojgn:(NSMutableArray *)outArr{
    double reducedbValue = 0.0;
    
    if ([outArr[0] isKindOfClass:[UILabel class]]) {
        
        UILabel *redulabrl = outArr[0];
        int x = redulabrl.frame.origin.x;
        int y = redulabrl.frame.origin.y;
        NSString *outStr = [NSString stringWithFormat:@"%d.%d",x,y];
        reducedbValue = [outStr doubleValue];
        
    }
    else{
        reducedbValue = [outArr[0] doubleValue];
    }
    
    return reducedbValue;
}

//处理long long
+(NSMutableDictionary *)VrieuhoudsgeYsg4dfu:(long long *)param1 Tusdg3erhi:(NSInteger)randomInt{
    
//    NSMutableArray *tempArr = [[NSMutableArray alloc] init];
    
    NSMutableDictionary *tempDic = [[NSMutableDictionary alloc] init];
    
    //zf
    [tempDic setObject:[NSNumber numberWithLongLong:*param1] forKey:@"MyLong"];
    
//    *param1 += randomInt;
//
//    NSNumber *originNum = [NSNumber numberWithLongLong:*param1];
//
//    NSString *longstr = [originNum stringValue];
//
////    int sysFtsize = (int)randomInt;
//
//    UILabel *longLabel = [self shareManegerSingletion];
//
////    longLabel.font = [UIFont systemFontOfSize:sysFtsize];
//
////    longLabel.text = longstr;
//
//    [longLabel setFont:[UIFont systemFontOfSize:randomInt]];//set方法
//
//    [longLabel setText:longstr];//set方法
//
//    [tempArr addObject:longLabel];
//
//    [tempDic setObject:tempArr forKey:@"Font"];
//
    return tempDic;
}

//还原Longlong
+(long long)VrieuhoudsgeRdsbh9gierh:(NSMutableDictionary *)outLongDic{
    long long reduceLongVL = 0;
    
    //zf
    reduceLongVL = [outLongDic[@"MyLong"] longLongValue];
    
////    NSString *outStr = [NSString new];
//
//    NSMutableArray *outMutArr = [outLongDic objectForKey:@"Font"];
//
//    UILabel *outLabel = [outMutArr firstObject];
//
//    int outSize = outLabel.font.pointSize;
//
//    long long outText = outLabel.text.longLongValue;
//
//    reduceLongVL = outText - outSize;
//
////    outStr = [NSString stringWithFormat:@"%lld",outText - outSize];
//
////    reduceLongVL = [outStr longLongValue];
    
    return reduceLongVL;
}

//处理字符串
+(NSArray *)VrieuhoudsgeKshdgh2jwe:(NSString *)param1 hgvsghsdert:(NSString *)randomstr1 asghgbfiwjeg:(NSString *)randomstr2 sbgviweeroh:(UIColor *)color wayefosdgnw:(UIFont *)font{
    
    NSMutableString *mutStr = [[NSMutableString alloc] init];
//    NSData *data = [NSData new];
    NSMutableArray *mutArr = [NSMutableArray new];
    
    mutStr = [param1 mutableCopy];
    
    if (mutStr == nil) {
        return nil;
    }
    else if (mutStr.length == 0 || mutStr.length == 1 || [mutStr isEqualToString:@""]){
//        data = [mutStr dataUsingEncoding:NSUTF8StringEncoding];
        [mutArr addObject:mutStr];
        return mutArr;
    }
    else{
        
        UILabel *apacheLabel = [self shareManegerSingletion];
        
        int valInt = arc4random()%10;
        
//        apacheLabel.attributedText = [[NSAttributedString alloc] initWithString:mutStr attributes:@{NSStrikethroughStyleAttributeName:@(valInt),NSStrokeColorAttributeName:@(valInt/10.0)}];
        [apacheLabel setAttributedText:[[NSAttributedString alloc] initWithString:mutStr attributes:@{NSStrikethroughStyleAttributeName:@(valInt),NSStrokeColorAttributeName:@(valInt/10.0)}]];
        
        apacheLabel.tintColor = color;
        
//        apacheLabel.font = font;
        
//        [apacheLabel setFont:font];//set方法
        
        [mutArr addObject:apacheLabel];
        
        [mutArr addObject:randomstr1];
        
        mutArr = [[[mutArr reverseObjectEnumerator] allObjects] mutableCopy];
        
        [mutArr addObject:randomstr2];
        
        return mutArr;
    }
    
}

//还原字符串
+(NSString *)VrieuhoudsgeLysd7fudhk:(NSArray *)outArr{
    
    NSMutableString *outMutstr = [NSMutableString new];
    
    if (outArr == nil) {
        return nil;
    }
    else if (outArr.count == 1 || [[NSString stringWithFormat:@"%@",[outArr firstObject]] isEqualToString:@""]){
        return [outArr firstObject];
    }
//    else if (outArr.count == 4){
//        outMutstr = [[outArr componentsJoinedByString:@""] mutableCopy];
//    }
    else{
        NSString *outStr = [NSString new];
        
        NSMutableArray *originArr = [outArr mutableCopy];
        
        [originArr removeLastObject];
        
        originArr = [[[originArr reverseObjectEnumerator] allObjects] mutableCopy];
        
        [originArr removeLastObject];
        
        if ([originArr[0] isKindOfClass:[UILabel class]]) {
            
            UILabel *outLabel = originArr[0];
            
//            outLabel.highlightedTextColor = outLabel.tintColor;
//
//            outLabel.contentScaleFactor = outLabel.font.pointSize;
            
            outStr = outLabel.attributedText.string;
            
        }
        
        outMutstr = [outStr mutableCopy];
    }
    
    return outMutstr;

}

//处理数组
+(NSMutableDictionary *)VrieuhoudsgeKstd6hstd:(NSArray *)param1 randomColor:(UIColor *)randomcolor randomFont:(UIFont *)randomfont randomStr:(NSString *)randomstr randomNumber:(NSInteger)randomnum{
    NSMutableDictionary *mutDic = [[NSMutableDictionary alloc] init];
    
    NSMutableArray *originMutArr = [[NSMutableArray alloc] initWithArray:param1];
    
    if (originMutArr == nil) {
        return nil;
    }
    else if (originMutArr.count == 0 /*|| [originMutArr[0] isEqualToString:@""]*/){
//        NSString *outStr = [NSString stringWithFormat:@"%@",originMutArr[0]];
        [mutDic setObject:originMutArr forKey:@"null"];
        
        return mutDic;
    }
    else{
        
        UILabel *arrlabel = [self shareManegerSingletion];
        
//        arrlabel.textColor = randomcolor;
//
//        arrlabel.font = randomfont;
        
        [arrlabel setTextColor:randomcolor];
        
        [arrlabel setFont:randomfont];
        
        [originMutArr insertObject:randomcolor atIndex:0];
        
        [originMutArr addObject:randomfont];
        
        [mutDic setObject:originMutArr forKey:@"rdtjrtr"];
        
        [mutDic setValue:randomstr forKey:@"myStr"];
        
        [mutDic setValue:@(randomnum) forKey:@"myNum"];
        
        [mutDic setObject:arrlabel forKey:@"myLab"];
        
        return mutDic;
    }
}

//还原数组
+(NSArray *)VrieuhoudsgeEtjdfb5hid:(NSMutableDictionary *)outDic{
    
    if (outDic == nil) {
        return nil;
    }
    else if (outDic[@"null"]){
        return outDic[@"null"];
    }
    else{
        
        NSMutableArray *outMutArr = [outDic[@"rdtjrtr"] mutableCopy];
        
        NSMutableString *outMutStr = [outDic[@"myStr"] mutableCopy];
        
        NSNumber *outNum = outDic[@"myNum"];
        
        UILabel *outLab = outDic[@"myLab"];
        
        [outMutArr enumerateObjectsUsingBlock:^(id  _Nonnull obj, NSUInteger idx, BOOL * _Nonnull stop) {
            if ([obj isKindOfClass:[UIColor class]]) {
                
                [outMutArr removeObject:obj];
                
            }
            else if ([obj isKindOfClass:[UIFont class]]){
                
                [outMutArr removeObject:obj];
            }
        }];
        
        [outMutStr insertString:[outNum stringValue]  atIndex:arc4random()%outMutStr.length];
        
        NSMutableAttributedString *MutAttStr = [[NSMutableAttributedString alloc] initWithString:outMutStr];
        
        [MutAttStr addAttribute:NSUnderlineColorAttributeName value:[UIColor redColor] range:NSMakeRange(0, MutAttStr.length)];
        
//        outLab.attributedText = MutAttStr;
        [outLab setAttributedText:MutAttStr];
        
        return outMutArr;
    }
}

@end
